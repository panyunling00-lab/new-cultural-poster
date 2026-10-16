"""Behavioral regression tests for design-free-v1 and profile switching.

python test_design_free.py
"""
import copy
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from PIL import Image
from build_prompt import build, candidate_pool, MONTAGE_LAYOUTS, people_policy, people_directive
from check_poster import evaluate
from decision_tree import decide
from typography_policy import (DEFAULTS, DEFAULT_PROFILE, PROFILE_FILES, load_profile,
                               default_font_sizes, geometry_checks, prompt_rules, review_typography)

ROOT=Path(__file__).resolve().parents[1]
FREE='design-free-v1'
SMALL='small-type-refined-v1'
FREE_P=load_profile(FREE)
SMALL_P=load_profile(SMALL)


def evidence(profile=FREE):
    base={'profile_id':profile,'evidence':'Synthetic test fixture evidence, not an actual poster review.'}
    if profile==FREE:
        base.update(intended_size_readable=True,exact_copy_verified=True,no_pseudo_text=True,facts_preserved=True)
    else:
        base.update(graphic_primary=True,subject_clearance_verified=True,negative_space_ratio=0.4,
                    intended_size_readable=True)
    return base


def brief_fixture(profile=FREE, layout='layered-depth'):
    brief=json.loads((ROOT/'templates/prompt-brief-example.json').read_text(encoding='utf-8'))
    brief.update(typography_profile=profile,layout=layout,language='zh',
                 reference_mode='features',text_mode='integrated')
    brief['canvas']='portrait A4, 210:297'
    brief['canvas_spec']={'ratio':'210:297','source':'synthetic fixture','verbatim':'portrait 210:297'}
    brief['source_audit']={'complete':True,'documents':[{'path':'synthetic fixture','pages':1,'read_pages':[1]}],'unresolved':[]}
    brief['source_copy']=[dict(id=x['id'],text=x['text'],source='synthetic fixture',required=True) for x in brief['copy_items']]
    style=next((ROOT/'assets/style-references'/brief['style']).glob('*.jpg'))
    layout_ref=next((ROOT/'assets/composition-references').glob('*/'+layout+'/*.png'))
    brief['references']=[dict(path=str(path),role=role,definition_id=brief[role],inspected=True,
                              borrowed_features=['fixture feature']) for role,path in [('style',style),('layout',layout_ref)]]
    return brief


class DesignFreeGeometryTests(unittest.TestCase):
    def test_large_overlapping_mixed_and_path_measurements_pass(self):
        items=[{'id':'title','role':'title','direction':'mixed','font_size_px':400,'bbox':[0,0,1000,1000]},
               {'id':'body','role':'body','direction':'path','font_size_px':200,'bbox':[50,50,900,900]}]
        result=geometry_checks(1000,1000,items,[[0,0,1000,1000]],profile=FREE)
        self.assertEqual(result['status'],'pass')
        self.assertEqual(result['failures'],[])
        self.assertIsNone(result['title_block_ratio'])
        self.assertGreater(result['text_block_area_ratio'],0)

    def test_geometry_is_descriptive_not_a_verdict(self):
        result=geometry_checks(1000,1000,[{'id':'title','role':'title','direction':'horizontal','font_size_px':900,'bbox':[0,0,1000,1000]}],profile=FREE)
        self.assertEqual(result['status'],'pass')
        self.assertIn('descriptive',result['note'])
        self.assertEqual(result['profile_id'],FREE)

    def test_invalid_measurements_still_rejected(self):
        with self.assertRaises(ValueError): geometry_checks(0,100,[],profile=FREE)
        with self.assertRaises(ValueError): geometry_checks(100,100,[{'id':'x','bbox':[0,0,101,100]}],profile=FREE)
        with self.assertRaises(ValueError): geometry_checks(100,100,{'not':'a list'},profile=FREE)
        with self.assertRaises(ValueError): geometry_checks(100,100,[{'id':'','role':'title','bbox':[0,0,50,50],'font_size_px':10}],profile=FREE)
        with self.assertRaises(ValueError): geometry_checks(100,100,[{'id':'x','role':'title','bbox':[0,0,50,50],'font_size_px':0}],profile=FREE)
        with self.assertRaises(ValueError): geometry_checks(100,100,[{'id':'x','role':'title','direction':'diagonal','bbox':[0,0,50,50],'font_size_px':10}],profile=FREE)
        with self.assertRaises(ValueError): geometry_checks(100,100,[{'id':'x','role':'heading','bbox':[0,0,50,50],'font_size_px':10}],profile=FREE)
        duplicate=[{'id':'x','role':'title','bbox':[0,0,50,50],'font_size_px':10}]*2
        with self.assertRaises(ValueError): geometry_checks(100,100,duplicate,profile=FREE)
        with self.assertRaises(ValueError): geometry_checks(100,100,[],[[0,0,200,200]],profile=FREE)


class DesignFreeReviewTests(unittest.TestCase):
    def test_four_flags_fail_and_missing(self):
        for flag in ('intended_size_readable','exact_copy_verified','no_pseudo_text','facts_preserved'):
            broken=evidence(); broken[flag]=False
            self.assertEqual(review_typography(broken,1000,1000,'final_poster',profile=FREE)['status'],'fail')
            missing=evidence(); del missing[flag]
            self.assertEqual(review_typography(missing,1000,1000,'final_poster',profile=FREE)['status'],'unknown')

    def test_complete_evidence_passes_without_area_metrics(self):
        self.assertEqual(review_typography(evidence(),1000,1000,'final_poster',profile=FREE)['status'],'pass')

    def test_empty_or_unbound_review_is_unknown(self):
        self.assertEqual(review_typography({},1000,1000,'final_poster',profile=FREE)['status'],'unknown')
        self.assertEqual(review_typography(None,1000,1000,'final_poster',profile=FREE)['status'],'unknown')

    def test_profile_id_must_match_active_profile(self):
        self.assertEqual(review_typography(evidence(SMALL),1000,1000,'final_poster',profile=FREE)['status'],'unknown')
        self.assertEqual(review_typography(evidence(FREE),1000,1000,'final_poster',profile=SMALL)['status'],'unknown')

    def test_items_are_optional(self):
        record=evidence()
        self.assertNotIn('items',record)
        self.assertEqual(review_typography(record,1000,1000,'final_poster',profile=FREE)['status'],'pass')


class ProfileSelectionTests(unittest.TestCase):
    def test_defaults_pointer_and_profile_ids(self):
        self.assertEqual(DEFAULTS['default_profile'],FREE)
        self.assertEqual(DEFAULT_PROFILE,FREE)
        self.assertEqual(FREE_P['id'],FREE)
        self.assertEqual(SMALL_P['id'],SMALL)
        self.assertEqual(PROFILE_FILES[SMALL],'typography-small-type.json')
        with self.assertRaises(ValueError): load_profile('unknown-profile')

    def test_candidate_pool_is_category_driven_under_both_profiles(self):
        for category in 'ABCDEFGH':
            free=candidate_pool({'categories':[category]})
            small=candidate_pool({'categories':[category],'typography_profile':SMALL})
            self.assertEqual(free,small)
            for layout in MONTAGE_LAYOUTS:
                self.assertNotIn(layout,free); self.assertNotIn(layout,small)
        combined=candidate_pool({'categories':list('ABCDEFGH')})
        # big-type-only belongs to no category row; disorder-layout and
        # full-bleed-image-overlay stay only where R7 lists them (F / B,E).
        self.assertNotIn('big-type-only',combined)

    def test_people_policy_resolution(self):
        self.assertEqual(people_policy({'categories':['A']}),'forbidden')
        self.assertEqual(people_policy({'categories':['C']}),'forbidden')
        self.assertEqual(people_policy({'categories':['B']}),'allowed')
        self.assertEqual(people_policy({'categories':['E']}),'allowed')
        self.assertEqual(people_policy({'categories':['B','C']}),'allowed')
        self.assertEqual(people_policy({'categories':['C'],'specialism':'market'}),'allowed')
        self.assertEqual(people_policy({'categories':['A'],'reference_people':'only-people'}),'allowed')
        self.assertEqual(people_policy({'categories':['A'],'reference_people':'people-plus-content'}),'avoid')
        self.assertEqual(people_policy({'categories':['A'],'people_policy':'allowed'}),'allowed')
        self.assertEqual(people_policy({'categories':['B'],'people_policy':'forbidden'}),'forbidden')
        with self.assertRaises(ValueError): people_policy({'categories':['A'],'people_policy':'maybe'})
        with self.assertRaises(ValueError): people_policy({'categories':['A'],'reference_people':'some-people'})
        for policy in ('forbidden','avoid','allowed'):
            self.assertNotEqual(people_directive(policy,'zh'),people_directive(policy,'en'))
            self.assertEqual(people_directive(policy),people_directive(policy,'zh'))
            with self.assertRaises(ValueError): people_directive(policy,'fr')
        with self.assertRaises(ValueError): people_directive('unknown')

    def test_default_font_sizes_differ(self):
        self.assertNotEqual(default_font_sizes(1000,1500,FREE),default_font_sizes(1000,1500,SMALL))

    def test_prompt_rules_are_profile_and_language_specific(self):
        zh_free=prompt_rules(FREE,'zh'); en_free=prompt_rules(FREE,'en')
        zh_small=prompt_rules(SMALL,'zh'); en_small=prompt_rules(SMALL,'en')
        self.assertEqual(len({zh_free,en_free,zh_small,en_small}),4)
        self.assertEqual(prompt_rules(FREE),zh_free)
        nominal=f"{SMALL_P['title_base_font_short_side_ratio']*SMALL_P['text_scale_weight']*1000/1000:.3f}"
        self.assertIn(nominal,en_small)
        self.assertIn(f"{SMALL_P['title_font_short_side_ratio_max']:.3f}",en_small)
        with self.assertRaises(ValueError): prompt_rules(FREE,'fr')
        with self.assertRaises(ValueError): prompt_rules('unknown-profile')

    def test_build_runs_and_respects_big_type_only(self):
        original=brief_fixture(FREE,'big-type-only')
        original['user_layout_override']=True
        snapshot=copy.deepcopy(original)
        result=build(original)
        self.assertEqual(result['typography_profile'],FREE)
        self.assertEqual(result['production_notes']['profile'],FREE)
        self.assertEqual(result['rendering_policy']['id'],FREE)
        self.assertNotIn('big-type-only',result['candidate_pool'])
        self.assertIn('design-free-v1',result['image_prompt'])
        self.assertIn('人物规则',result['image_prompt'])
        self.assertEqual(original,snapshot)

    def test_build_requires_override_for_out_of_pool_layout(self):
        brief=brief_fixture(FREE,'big-type-only')
        with self.assertRaises(ValueError): build(brief)

    def test_build_rejects_big_type_only_under_small_type(self):
        brief=brief_fixture(SMALL,'big-type-only')
        brief['user_layout_override']=True
        with self.assertRaises(ValueError): build(brief)

    def test_build_rejects_montage_layout_under_every_profile(self):
        for profile in (FREE,SMALL):
            for layout in MONTAGE_LAYOUTS:
                brief=brief_fixture(profile,layout); brief['user_layout_override']=True
                with self.assertRaises(ValueError): build(brief)

    def test_decision_tree_is_profile_aware(self):
        base={'categories':['C'],'relation':'process','motion':'static','copy_density':'low','mood':'quiet'}
        free=decide(dict(base,user_layout='big-type-only'))
        self.assertEqual(free['status'],'fixed_layout')
        small=decide(dict(base,user_layout='big-type-only',typography_profile=SMALL))
        self.assertEqual(small['status'],'conflict')
        for profile in (FREE,SMALL):
            for layout in MONTAGE_LAYOUTS:
                self.assertEqual(decide(dict(base,user_layout=layout,typography_profile=profile))['status'],'conflict')

    def test_input_error_still_reports_missing_fields(self):
        self.assertEqual(decide({'categories':['C']})['status'],'needs_analysis')


class QualityGateTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.folder=Path(self.temp.name)
        self.image=self.folder/'A.png'; Image.new('RGB',(1000,1000),'white').save(self.image)

    def tearDown(self):
        self.temp.cleanup()

    def request(self,profile=FREE):
        return {'image':str(self.image),'stage':'final_poster','typography_profile':profile,'visual_review':{
            'image_sha256':hashlib.sha256(self.image.read_bytes()).hexdigest(),'stage':'final_poster',
            'hard_gates':{'H'+str(i):{'status':'pass','evidence':'Synthetic software evidence'} for i in range(1,9)},
            'dimensions':{k:{'score':5,'evidence':'Synthetic software evidence'} for k in 'ABCDEFG'},
            'typography':evidence(profile)}}

    def test_report_records_active_profile(self):
        self.assertEqual(evaluate(self.request(FREE))['typography_profile'],FREE)

    def test_quality_cannot_pass_incorrect_copy(self):
        req=self.request(); self.assertEqual(evaluate(req)['decision'],'pass')
        req['visual_review']['typography']['exact_copy_verified']=False
        result=evaluate(req)
        self.assertEqual(result['total'],100); self.assertEqual(result['decision'],'revise')
        self.assertIn('H1',result['known_failures'])

    def test_h8_missing_unknown_and_failure_block(self):
        req=self.request(); del req['visual_review']['hard_gates']['H8']
        self.assertEqual(evaluate(req)['decision'],'needs verification')
        req=self.request(); req['visual_review']['hard_gates']['H8']['status']='fail'
        self.assertEqual(evaluate(req)['decision'],'revise')

    def test_request_profile_overrides_recorded_id(self):
        req=self.request(FREE)
        req['typography_profile']=SMALL
        self.assertEqual(evaluate(req)['decision'],'needs verification')


if __name__=='__main__':
    unittest.main(verbosity=2)
