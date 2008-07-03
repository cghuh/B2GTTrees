import FWCore.ParameterSet.Config as cms

# from HLTrigger/btau/data/jetTag/softmuonL3.cff - b HLT modules for Level 3.
import HLTrigger.btau.jetTag.hltJetTag_cfi
hltBSoftmuonL3filter = HLTrigger.btau.jetTag.hltJetTag_cfi.hltJetTag.clone()

import HLTrigger.btau.jetTag.getJetsFromHLTobject_cfi
hltBSoftmuonHLTJets = HLTrigger.btau.jetTag.getJetsFromHLTobject_cfi.getJetsFromHLTobject.clone()
hltBSoftmuonHLTJets.jets = 'hltBSoftmuonL3filter'

# from ConfDB
import HLTrigger.btau.jetTag.hltJetTag_cfi
hltBSoftmuonByDRL3filter = HLTrigger.btau.jetTag.hltJetTag_cfi.hltJetTag.clone()

import HLTrigger.btau.jetTag.getJetsFromHLTobject_cfi
hltBSoftmuonHLTJetsByDR = HLTrigger.btau.jetTag.getJetsFromHLTobject_cfi.getJetsFromHLTobject.clone()
hltBSoftmuonHLTJetsByDR.jets = 'hltBSoftmuonByDRL3filter'

# from ConfDB (relaxed triggers)
import HLTrigger.btau.jetTag.hltJetTag_cfi
hltBSoftmuonL3filterRelaxed = HLTrigger.btau.jetTag.hltJetTag_cfi.hltJetTag.clone()

import HLTrigger.btau.jetTag.getJetsFromHLTobject_cfi
hltBSoftmuonHLTJetsRelaxed = HLTrigger.btau.jetTag.getJetsFromHLTobject_cfi.getJetsFromHLTobject.clone()
hltBSoftmuonHLTJetsRelaxed.jets = 'hltBSoftmuonL3filterRelaxed'

# (re)generate some productes used by the validation path
# only run on L3 events
require_hltBSoftmuonL3BJetTags = cms.EDFilter("RequireModule",
    requirement = cms.InputTag("hltBSoftmuonL3BJetTags","","HLT")
)

# same, for calibration trigger
# only run on L3 events (HLT_BTagMu_Jet20_Calib path)
require_hltBSoftmuonL3BJetTagsByDR = cms.EDFilter("RequireModule",
    requirement = cms.InputTag("hltBSoftmuonL3BJetTagsByDR","","HLT")
)

# same, for relaxed triggers
# only run on L3 events
require_hltBSoftmuonL3BJetTagsRelaxed = cms.EDFilter("RequireModule",
    requirement = cms.InputTag("hltBSoftmuonL3BJetTagsRelaxed","","HLT")
)

hltBSoftmuonExtra = cms.Sequence(require_hltBSoftmuonL3BJetTags*hltBSoftmuonL3filter*hltBSoftmuonHLTJets)
hltBSoftmuonExtraByDR = cms.Sequence(require_hltBSoftmuonL3BJetTagsByDR*hltBSoftmuonByDRL3filter*hltBSoftmuonHLTJetsByDR)
hltBSoftmuonExtraRelaxed = cms.Sequence(require_hltBSoftmuonL3BJetTagsRelaxed*hltBSoftmuonL3filterRelaxed*hltBSoftmuonHLTJetsRelaxed)

hltBSoftmuonL3filter.JetTag = 'hltBSoftmuonL3BJetTags::HLT'
hltBSoftmuonL3filter.MinTag = 0.7           ## pT_rel in GeV/c

hltBSoftmuonByDRL3filter.JetTag = 'hltBSoftmuonL3BJetTagsByDR::HLT'
hltBSoftmuonByDRL3filter.MinTag = 0.5       ## 1 if dR < 0.5, 0 otherwise

hltBSoftmuonL3filterRelaxed.JetTag = 'hltBSoftmuonL3BJetTagsRelaxed::HLT'
hltBSoftmuonL3filterRelaxed.MinTag = 0.5    ## pT_rel in GeV/c
