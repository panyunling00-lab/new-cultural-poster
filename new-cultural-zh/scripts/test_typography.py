"""Regression checks for observable scale, rendering and quality-gate behavior.

python test_typography.py
Optional POSTER_TEST_FONT supplies a Latin-capable local fixture for rendering tests.
Test font use is restricted to synthetic temporary fixtures, never production routing.
"""
import copy
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from PIL import Image, ImageDraw
from typography_policy import (DEFAULTS, DEFAULT_PROFILE, PROFILE_FILES, load_profile,
                               default_font_sizes, geometry_checks, prompt_rules, review_typography)
from build_prompt import build, candidate_pool
from check_poster import evaluate
from render_text_layers import render
from composite_text_layer import composite

ROOT = Path(__file__).resolve().parents[1]
SMALL = 'small-type-refined-v1'
FREE = 'design-free-v1'
SMALL_P = load_profile(SMALL)
FREE_P = load_profile(FREE)


def small_nominal_size(short=1000):
    return short * SMALL_P['title_base_font_short_side_ratio'] * SMALL_P['text_scale_weight']


def item(identifier='title', role='title', bbox=None, size=None, direction='horizontal'):
    return {'id':identifier, 'role':role, 'direction':direction,
            'bbox':bbox or [100, 140, 800, 180], 'font_size_px':small_nominal_size() if size is None else size}


def visual(items=None, profile=SMALL):
    return {'profile_id':profile, 'items':[item()] if items is None else items,
            'graphic_primary':True, 'subject_clearance_verified':True,
            'negative_space_ratio':0.4, 'intended_size_readable':True,
            'evidence':'Synthetic fixture: protected geometric subject occupies the central region; measured text is in upper and lower quiet zones.'}


def prompt_fixture():
    # Synthetic host inspection claims test assembly only, not visual inspection.
    brief=json.loads((ROOT/'templates/prompt-brief-example.json').read_text(encoding='utf-8'))
    # The example brief documents the default profile; these are small-type tests,
    # so pin the profile explicitly instead of inheriting the example's choice.
    brief.update(typography_profile=SMALL, language='en', text_mode='overlay', reference_mode='features')
    brief['canvas_spec']={'ratio':'210:297','source':'synthetic fixture','verbatim':'portrait 210:297'}
    brief['source_audit']={'complete':True,'documents':[{'path':'synthetic fixture','pages':1,'read_pages':[1]}],'unresolved':[]}
    brief['source_copy']=[dict(id=x['id'],text=x['text'],source='synthetic fixture',required=True) for x in brief['copy_items']]
    style=next((ROOT/'assets/style-references'/brief['style']).glob('*.jpg'))
    layout=next((ROOT/'assets/composition-references').glob('*/'+brief['layout']+'/*.png'))
    brief['references']=[dict(path=str(path),role=role,definition_id=brief[role],inspected=True,
                              borrowed_features=['fixture feature']) for role,path in [('style',style),('layout',layout)]]
    return brief


class PolicyTests(unittest.TestCase):
    def test_scale_defaults_follow_canvas_short_side(self):
        sizes=default_font_sizes(1000,1500,SMALL)
        self.assertAlmostEqual(sizes['title'],small_nominal_size(1000))
        self.assertEqual(default_font_sizes(1500,1000,SMALL),sizes)
        self.assertAlmostEqual(sizes['subtitle'],small_nominal_size(1000)*SMALL_P['subtitle_title_ratio'])
        self.assertAlmostEqual(sizes['body'],small_nominal_size(1000)*SMALL_P['body_title_ratio'])

    def test_complete_horizontal_title_boundary(self):
        self.assertEqual(geometry_checks(1000,1500,[item(bbox=[100,120,200,420])],profile=SMALL)['status'],'pass')
        result=geometry_checks(1000,1500,[item(bbox=[100,120,200,421])],profile=SMALL)
        self.assertEqual(result['status'],'fail')
        self.assertGreater(result['title_block_ratio'],SMALL_P['title_block_max_ratio'])

    def test_vertical_uses_width_even_when_height_would_pass(self):
        self.assertEqual(geometry_checks(1000,1500,[item(bbox=[100,120,300,500],direction='vertical')],profile=SMALL)['status'],'pass')
        self.assertEqual(geometry_checks(1000,1500,[item(bbox=[100,120,301,300],direction='vertical')],profile=SMALL)['status'],'fail')

    def test_title_items_are_measured_together(self):
        items=[item(bbox=[100,120,250,160]),item('translation',bbox=[100,450,250,490])]
        result=geometry_checks(1000,1500,items,profile=SMALL)
        self.assertEqual(result['status'],'fail')
        self.assertAlmostEqual(result['title_block_ratio'],370/1500)

    def test_body_role_cap_uses_actual_reduced_title(self):
        items=[item(size=40),item('body','body',[100,1200,700,1240],13)]
        self.assertEqual(geometry_checks(1000,1500,items,profile=SMALL)['status'],'fail')
        items[1]['font_size_px']=12
        self.assertEqual(geometry_checks(1000,1500,items,profile=SMALL)['status'],'pass')

    def test_margins_and_subject_clearance(self):
        self.assertEqual(geometry_checks(1000,1500,[item(bbox=[79,140,700,180])],profile=SMALL)['status'],'fail')
        self.assertEqual(geometry_checks(1000,1500,[item()],[[100,200,800,900]],profile=SMALL)['status'],'fail')

    def test_overlapping_or_crowded_text_fails(self):
        items=[item(),item('subtitle','subtitle',[100,190,800,210],22)]
        self.assertEqual(geometry_checks(1000,1500,items,profile=SMALL)['status'],'fail')

    def test_large_text_block_area_fails(self):
        result=geometry_checks(1000,1500,[item('body','body',[100,120,900,1200],12)],profile=SMALL)
        self.assertEqual(result['status'],'fail')
        self.assertGreater(result['text_block_area_ratio'],SMALL_P['text_block_area_ratio_max'])

    def test_visual_whitespace_and_hierarchy_are_required(self):
        v=visual(); v['negative_space_ratio']=SMALL_P['negative_space_ratio_min']-0.01
        self.assertEqual(review_typography(v,1000,1500,'final_poster',profile=SMALL)['status'],'fail')
        v=visual(); v['graphic_primary']=False
        self.assertEqual(review_typography(v,1000,1500,'final_poster',profile=SMALL)['status'],'fail')
        v=visual(); del v['intended_size_readable']
        self.assertEqual(review_typography(v,1000,1500,'final_poster',profile=SMALL)['status'],'unknown')

    def test_key_visual_does_not_invent_text(self):
        self.assertEqual(review_typography(visual([]),1000,1500,'key_visual',profile=SMALL)['status'],'pass')
        self.assertEqual(review_typography(visual([]),1000,1500,'final_poster',profile=SMALL)['status'],'unknown')

    def test_both_prompt_modes_inherit_policy_and_preserve_copy(self):
        brief=prompt_fixture()
        overlay=build(brief)
        self.assertEqual(overlay['rendering_policy']['text_scale_weight'],SMALL_P['text_scale_weight'])
        self.assertEqual(overlay['copy_manifest'],brief['copy_items'])
        self.assertTrue('text-free visual background' in overlay['image_prompt'] or '无字视觉底图' in overlay['image_prompt'])
        brief['text_mode']='integrated'; brief['typesetting_available']=False
        integrated=build(brief)
        self.assertEqual(integrated['rendering_policy'],overlay['rendering_policy'])
        for copy_item in brief['copy_items']:
            self.assertIn(copy_item['text'],integrated['image_prompt'])
        self.assertIn(f"absolute cap {SMALL_P['title_block_max_ratio']:.0%}",integrated['image_prompt'])

    def test_legacy_text_dominant_layout_cannot_bypass_profile(self):
        brief=prompt_fixture()
        for category in 'ABCDEFGH':
            self.assertNotIn('big-type-only',candidate_pool({'categories':[category],'typography_profile':SMALL}))
        brief['layout']='big-type-only'; brief['user_layout_override']=True
        with self.assertRaises(ValueError): build(brief)

    def test_negative_list_is_injected_in_the_prompt_language(self):
        brief=prompt_fixture()
        english=build(brief)
        chinese=build(dict(brief,language='zh'))
        self.assertGreaterEqual(len(english['negative_prompt']),10)
        self.assertEqual(len(english['negative_prompt']),len(chinese['negative_prompt']))
        self.assertIn(english['negative_prompt'][0],english['image_prompt'])
        self.assertIn(chinese['negative_prompt'][0],chinese['image_prompt'])
        self.assertNotIn(chinese['negative_prompt'][0],english['image_prompt'])
        with self.assertRaises(ValueError): build(dict(brief,language='fr'))

    def test_quality_100_points_cannot_offset_typography_failure(self):
        with tempfile.TemporaryDirectory() as folder:
            image=Path(folder)/'fixture.png'; Image.new('RGB',(1000,1500),'white').save(image)
            req={'image':str(image),'stage':'final_poster','visual_review':{
                'image_sha256':hashlib.sha256(image.read_bytes()).hexdigest(),'stage':'final_poster',
                'hard_gates':{f'H{i}':{'status':'pass','evidence':'Synthetic testing evidence'} for i in range(1,9)},
                'dimensions':{key:{'score':5,'evidence':'Synthetic testing evidence'} for key in 'ABCDEFG'},
                'typography':visual()}}
            self.assertEqual(evaluate(req)['decision'],'pass')
            req['visual_review']['typography']['items'][0]['bbox']=[100,120,300,430]
            result=evaluate(req)
            self.assertEqual(result['total'],100)
            self.assertEqual(result['decision'],'revise')
            self.assertIn('H1',result['known_failures'])
            del req['visual_review']['typography']
            self.assertEqual(evaluate(req)['decision'],'needs verification')


class ProfileSwitchTests(unittest.TestCase):
    def test_defaults_file_is_a_pointer(self):
        self.assertEqual(DEFAULTS['default_profile'],FREE)
        self.assertEqual(DEFAULTS['profiles'][SMALL],'typography-small-type.json')
        self.assertEqual(DEFAULTS['profiles'][FREE],'typography-design-free.json')
        self.assertEqual(DEFAULT_PROFILE,FREE)
        self.assertNotIn('title_base_font_short_side_ratio',DEFAULTS)
        with self.assertRaises(ValueError): load_profile('no-such-profile')

    def test_default_font_sizes_differ_between_profiles(self):
        free=default_font_sizes(1000,1500,FREE)
        small=default_font_sizes(1000,1500,SMALL)
        self.assertNotEqual(free,small)
        self.assertAlmostEqual(free['title'],1000*FREE_P['renderer_title_short_side_ratio'])
        self.assertAlmostEqual(free['subtitle'],1000*FREE_P['renderer_subtitle_short_side_ratio'])
        self.assertAlmostEqual(free['body'],1000*FREE_P['renderer_body_short_side_ratio'])

    def test_same_measurements_flip_from_fail_to_pass(self):
        items=[item(bbox=[150,150,500,900],size=400),
               item('body','body',[150,200,500,850],200)]
        self.assertEqual(geometry_checks(1000,1500,items,profile=SMALL)['status'],'fail')
        result=geometry_checks(1000,1500,items,profile=FREE)
        self.assertEqual(result['status'],'pass')
        self.assertIsNone(result['title_block_ratio'])
        self.assertGreater(result['text_block_area_ratio'],0)
        self.assertIn('descriptive',result['note'])

    def test_design_free_accepts_mixed_and_path_directions(self):
        items=[{'id':'title','role':'title','direction':'mixed','font_size_px':400,'bbox':[0,0,1000,1000]},
               {'id':'body','role':'body','direction':'path','font_size_px':200,'bbox':[50,50,900,900]}]
        self.assertEqual(geometry_checks(1000,1000,items,[[0,0,1000,1000]],profile=FREE)['status'],'pass')
        with self.assertRaises(ValueError):
            geometry_checks(1000,1000,items,profile=SMALL)

    def test_design_free_rejects_only_malformed_measurements(self):
        with self.assertRaises(ValueError): geometry_checks(0,100,[],profile=FREE)
        with self.assertRaises(ValueError): geometry_checks(100,100,[{'id':'x','bbox':[0,0,101,100]}],profile=FREE)
        with self.assertRaises(ValueError): geometry_checks(100,100,[{'id':'x','bbox':[0,0,50,50],'direction':'diagonal','font_size_px':10,'role':'title'}],profile=FREE)
        with self.assertRaises(ValueError): geometry_checks(100,100,[item(bbox=[0,0,50,50]),item(bbox=[0,0,50,50])],profile=FREE)

    def test_design_free_review_field_set(self):
        base={'profile_id':FREE,'intended_size_readable':True,'exact_copy_verified':True,
              'no_pseudo_text':True,'facts_preserved':True,'evidence':'Synthetic fixture evidence.'}
        self.assertEqual(review_typography(base,1000,1500,'final_poster',profile=FREE)['status'],'pass')
        for flag in ('intended_size_readable','exact_copy_verified','no_pseudo_text','facts_preserved'):
            broken=dict(base); broken[flag]=False
            self.assertEqual(review_typography(broken,1000,1500,'final_poster',profile=FREE)['status'],'fail')
            missing=dict(base); del missing[flag]
            self.assertEqual(review_typography(missing,1000,1500,'final_poster',profile=FREE)['status'],'unknown')
        # A small-type record is unknown under the design-free profile (mismatched id).
        self.assertEqual(review_typography(visual(),1000,1500,'final_poster',profile=FREE)['status'],'unknown')

    def test_prompt_rules_two_profiles_two_languages_distinct(self):
        blocks=[prompt_rules(FREE,'zh'),prompt_rules(FREE,'en'),
                prompt_rules(SMALL,'zh'),prompt_rules(SMALL,'en')]
        self.assertEqual(len(set(blocks)),4)
        self.assertEqual(prompt_rules(FREE),prompt_rules(FREE,'zh'))
        interpolated=f"{small_nominal_size(1000)/1000:.3f}"
        self.assertIn(interpolated,prompt_rules(SMALL,'en'))
        self.assertIn(f"{SMALL_P['title_font_short_side_ratio_max']:.3f}",prompt_rules(SMALL,'en'))
        with self.assertRaises(ValueError): prompt_rules(SMALL,'fr')

    def test_candidate_pool_is_category_driven_under_both_profiles(self):
        # Pools follow the R7 category mapping under BOTH profiles; no profile
        # appends layouts across categories any more.
        free_pool=candidate_pool({'categories':['A'],'typography_profile':FREE})
        small_pool=candidate_pool({'categories':['A'],'typography_profile':SMALL})
        self.assertEqual(free_pool,small_pool)
        combined=candidate_pool({'categories':list('ABCDEFGH')})
        self.assertNotIn('big-type-only',combined)
        for layout in ('modular-grid','split-horizontal','split-vertical'):
            self.assertNotIn(layout,free_pool); self.assertNotIn(layout,small_pool)


class RenderTests(unittest.TestCase):
    def setUp(self):
        default = os.environ.get('POSTER_TEST_FONT') or next(
            (c for c in ('/System/Library/Fonts/Hiragino Sans GB.ttc',
                         '/System/Library/Fonts/STHeiti Medium.ttc',
                         '/System/Library/Fonts/Supplemental/Arial Unicode.ttf',
                         '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf') if Path(c).is_file()), '')
        self.font=Path(default)
        if not self.font.is_file(): self.skipTest('No local synthetic Latin font fixture; set POSTER_TEST_FONT')
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.folder=Path(self.temp.name)
        self.background=self.folder/'background.png'
        im=Image.new('RGBA',(1000,1500),'#f4f0e8')
        ImageDraw.Draw(im).ellipse([270,450,730,1100],fill='#34544a'); im.save(self.background)
        self.request={'background':str(self.background),'typography_profile':SMALL,'supplied_fonts':[str(self.font)],
                      'subject_boxes':[[270,450,730,1100]],'items':[
                          {'id':'title','role':'title','text':'Culture & Form','font':str(self.font),'region':[80,120,920,380]},
                          {'id':'body','role':'venue','text':'Complete supplied details: Saturday, 10:00.','font':str(self.font),'region':[80,1200,920,1380]}]}

    def test_real_render_has_separate_layer_and_measured_small_type(self):
        report=render(self.request,self.folder/'horizontal')
        self.assertEqual(report['geometry']['status'],'pass')
        self.assertEqual(report['profile_id'],SMALL)
        self.assertEqual([i['text'] for i in report['items']],[i['text'] for i in self.request['items']])
        with Image.open(self.folder/'horizontal/text-layer.png') as layer:
            self.assertEqual(layer.mode,'RGBA')
            self.assertEqual(layer.getpixel((500,750))[3],0)
        with self.assertRaises(ValueError): render(self.request,self.folder/'horizontal')
        self.assertEqual(hashlib.sha256((self.folder/'horizontal/composed-preview.png').read_bytes()).hexdigest(),report['image_sha256'])

    def test_vertical_render_is_measured_on_width(self):
        self.request['items'][0].update(text='ART',direction='vertical',region=[80,120,260,400])
        report=render(self.request,self.folder/'vertical')
        title=report['items'][0]
        self.assertEqual(title['direction'],'vertical')
        self.assertAlmostEqual(report['geometry']['title_block_ratio'],(title['bbox'][2]-title['bbox'][0])/1000)

    def test_large_explicit_body_and_subject_overlap_are_rejected(self):
        req=copy.deepcopy(self.request); req['items'][1]['font_size_px']=40
        with self.assertRaises(ValueError): render(req,self.folder/'large-body')
        req=copy.deepcopy(self.request); req['subject_boxes']=[[90,100,900,350]]
        with self.assertRaises(ValueError): render(req,self.folder/'overlap')
        self.assertFalse((self.folder/'overlap/composed-preview.png').exists())

    def test_missing_glyph_and_unregistered_font_are_rejected(self):
        req=copy.deepcopy(self.request); req['items'][0]['text']='Missing \U0010ffff'
        with self.assertRaises(ValueError): render(req,self.folder/'missing-glyph')
        req=copy.deepcopy(self.request); req['supplied_fonts']=[]
        with self.assertRaises(ValueError): render(req,self.folder/'no-font')

    def test_dense_copy_cannot_shrink_below_floor(self):
        req=copy.deepcopy(self.request); req['items'][1]['text']='Long complete body copy. '*40
        with self.assertRaises(ValueError): render(req,self.folder/'dense-copy')
        self.assertFalse((self.folder/'dense-copy/composed-preview.png').exists())

    def test_design_free_render_allows_oversized_overlap(self):
        req={'background':str(self.background),'typography_profile':FREE,'supplied_fonts':[str(self.font)],
             'subject_boxes':[[270,450,730,1100]],'items':[
                 {'id':'title','role':'title','text':'A','font':str(self.font),'font_size_px':400,'region':[80,120,920,700]},
                 {'id':'body','role':'body','text':'B','font':str(self.font),'font_size_px':200,'region':[80,300,920,900]}]}
        report=render(req,self.folder/'free-overlap')
        self.assertEqual(report['geometry']['status'],'pass')
        self.assertEqual([i['font_size_px'] for i in report['items']],[400,200])


class CompositeTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.folder=Path(self.temp.name)
        base=Image.new('RGB',(800,1200),(128,128,128)); ImageDraw.Draw(base).rectangle([300,500,500,700],fill=(200,40,40)); base.save(self.folder/'base.png')
        light=Image.new('RGB',(800,1200),(0,0,0)); ImageDraw.Draw(light).rectangle([100,100,700,200],fill=(240,240,240)); light.save(self.folder/'light.png')
        dark=Image.new('RGB',(800,1200),(255,255,255)); ImageDraw.Draw(dark).rectangle([100,100,700,200],fill=(20,20,20)); dark.save(self.folder/'dark.png')
        mid=Image.new('RGB',(800,1200),(128,128,128)); mid.save(self.folder/'mid.png')

    def test_screen_and_multiply_keep_neutral_backgrounds(self):
        first=composite(self.folder/'base.png',self.folder/'light.png',self.folder/'c1.png',self.folder/'c1.json',(800,1200),'0,0,1,1','auto',1.0)
        self.assertEqual(first['typography_layer']['mode'],'screen')
        out=Image.open(self.folder/'c1.png')
        self.assertEqual(out.getpixel((400,900)),(128,128,128))
        self.assertGreater(out.getpixel((400,150))[0],220)
        cfg=composite(self.folder/'base.png',self.folder/'dark.png',self.folder/'c2.png',self.folder/'c2.json',(800,1200),'0.1,0.05,0.8,0.25','auto',1.0)
        self.assertEqual(cfg['typography_layer']['mode'],'multiply')
        self.assertEqual(Image.open(self.folder/'c2.png').getpixel((400,900)),(128,128,128))
        again=composite(self.folder/'base.png',self.folder/'light.png',self.folder/'c1.png',self.folder/'c1.json',(800,1200),'0,0,1,1','screen',1.0)
        self.assertEqual(again['output']['sha256'],first['output']['sha256'])

    def test_bad_layer_background_and_overwrite_are_rejected(self):
        with self.assertRaises(ValueError): composite(self.folder/'base.png',self.folder/'mid.png',self.folder/'c3.png',self.folder/'c3.json',(800,1200),'0,0,1,1','auto',1.0)
        with self.assertRaises(ValueError): composite(self.folder/'base.png',self.folder/'light.png',self.folder/'base.png',self.folder/'c4.json',(800,1200),'0,0,1,1','screen',1.0)

    def test_composite_mode_build_prompt_targets_layer_and_compositor(self):
        brief=prompt_fixture()
        brief['text_mode']='composite'
        result=build(brief)
        notes=result['production_notes']
        self.assertEqual(notes['mode'],'composite')
        self.assertEqual(notes['profile'],SMALL)
        self.assertIn('composite_text_layer.py',notes['compositor'])
        self.assertTrue('text-free visual background' in result['image_prompt'] or '无字视觉底图' in result['image_prompt'])
        self.assertEqual(notes['typesetting_items'],brief['copy_items'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
