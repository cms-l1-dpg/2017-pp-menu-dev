# 2017-pp-menu-dev
Collection of development menus for 2017 proton collision

https://twiki.cern.ch/twiki/bin/viewauth/CMS/HowToL1TriggerMenu

Tutorial
https://indico.cern.ch/event/623817/

---
### initial collection of seeds
---
  * [csv](https://github.com/cms-l1-dpg/2017-pp-menu-dev/blob/version-1/Apr12/L1MenuId.csv)
  * [xml](https://raw.githubusercontent.com/cms-l1-dpg/2017-pp-menu-dev/version-1/Apr12/L1Menu_20170412.xml)
---
### L1Menu_Collisions2017_dev_r2 [2017-05-03-tsg]
---
  * [csv](https://github.com/cms-l1-dpg/2017-pp-menu-dev/blob/2017-05-03-tsg/Apr12/L1MenuId.csv)
  * [xml](https://raw.githubusercontent.com/cms-l1-dpg/2017-pp-menu-dev/2017-05-03-tsg/Apr12/L1Menu_Collisions2017_dev_r2.xml)
---
### L1Menu_Collisions2017_dev_r3 [2017-05-17]
---
  * [csv](https://github.com/cms-l1-dpg/2017-pp-menu-dev/blob/2017-05-17/Apr12/L1MenuId.csv)
  * [xml](https://raw.githubusercontent.com/cms-l1-dpg/2017-pp-menu-dev/2017-05-17/Apr12/L1Menu_Collisions2017_dev_r3.xml)
    * updates from L1Menu_Collisions2017_dev_r2 [2017-05-03-tsg]
      * https://its.cern.ch/jira/browse/CMSLITDPG-95
      * https://its.cern.ch/jira/browse/CMSLITDPG-94
      * https://its.cern.ch/jira/browse/CMSLITDPG-87
      * https://its.cern.ch/jira/browse/CMSLITDPG-85
      * https://its.cern.ch/jira/browse/CMSLITDPG-84
      * Adding L1_DoubleJet_100_35_DoubleJet35_Mass_Min620
      * https://its.cern.ch/jira/browse/CMSLITDPG-82
      * https://its.cern.ch/jira/browse/CMSLITDPG-48
---
### L1Menu_Collisions2017_dev_r7 [2017-06-26]
---
  * [csv](https://github.com/cms-l1-dpg/2017-pp-menu-dev/blob/2017-06-26/Apr12/L1MenuId.csv)
  * [xml](https://raw.githubusercontent.com/cms-l1-dpg/2017-pp-menu-dev/2017-06-26/Apr12/L1Menu_Collisions2017_dev_r7.xml)
    * updates from L1Menu_Collisions2017_dev_r3 [2017-05-17] NB: compatible with L1Menu_Collisions2017_dev_r5_v3 deployed online 
      * https://its.cern.ch/jira/browse/CMSLITDPG-128
      * https://its.cern.ch/jira/browse/CMSLITDPG-113
      * https://its.cern.ch/jira/browse/CMSLITDPG-134
---
### L1Menu_Collisions2017_dev_r8 [2017-07-05]
---
  * [csv](https://github.com/cms-l1-dpg/2017-pp-menu-dev/blob/aeb7af17785fd8e059229a95240585482552dd34/Apr12/L1MenuId.csv)
  * [xml](https://raw.githubusercontent.com/cms-l1-dpg/2017-pp-menu-dev/30081c575ccca5362b42ce8be112b20d305f8cc6/Apr12/L1Menu_Collisions2017_dev_r8.xml)
    * updates from L1Menu_Collisions2017_dev_r7
      * https://its.cern.ch/jira/browse/CMSLITDPG-155?jql=labels%20%3D%20HLTv2
      * Incompatible changes
```
        renames
        =======
          https://its.cern.ch/jira/browse/CMSLITDPG-134
            L1_ETMHF80_HTT60er -> L1_ETMHF80_HTT60
            L1_ETMHF90_HTT60er -> L1_ETMHF90_HTT60
            L1_ETMHF100_HTT60er -> L1_ETMHF100_HTT60
            L1_ETMHF110_HTT60er -> L1_ETMHF110_HTT60
            L1_ETMHF120_HTT60er -> L1_ETMHF120_HTT60

          https://its.cern.ch/jira/browse/CMSLITDPG-152
            L1_Mu23_IsoEG10                               -> L1_Mu23_LooseIsoEG10
            L1_IsoEG24er2p1_HTT100er                      -> L1_LooseIsoEG24er2p1_HTT100er
            L1_IsoEG20er2p1_IsoTau25er2p1_dR_Min0p3       -> L1_LooseIsoEG20er2p1_IsoTau25er2p1_dR_Min0p3
            L1_IsoEG24er2p1_TripleJet_26er3p0_26_26er3p0  -> L1_LooseIsoEG24er2p1_TripleJet_26er3p0_26_26er3p0
            L1_IsoEG26er2p1_HTT100er                      -> L1_LooseIsoEG26er2p1_HTT100er
            L1_Mu5_IsoEG20                                -> L1_Mu5_LooseIsoEG20
            L1_IsoEG30er2p1_Jet34er3p0_dR_Min0p3          -> L1_LooseIsoEG30er2p1_Jet34er3p0_dR_Min0p3
            L1_Mu7_IsoEG23                                -> L1_Mu7_LooseIsoEG23
            L1_IsoEG18er2p1_IsoTau24er2p1_dR_Min0p3       -> L1_LooseIsoEG18er2p1_IsoTau24er2p1_dR_Min0p3
            L1_Mu20_IsoEG6                                -> L1_Mu20_LooseIsoEG6
            L1_DoubleEG_Iso23_10                          -> L1_DoubleEG_LooseIso23_10
            L1_DoubleEG_Iso24_10                          -> L1_DoubleEG_LooseIso24_10
            L1_Mu7_IsoEG20                                -> L1_Mu7_LooseIsoEG20
            L1_IsoEG28er2p1_Jet34er3p0_dR_Min0p3          -> L1_LooseIsoEG28er2p1_Jet34er3p0_dR_Min0p3
            L1_TripleEG_Iso20_10_5                        -> L1_TripleEG_LooseIso20_10_5
            L1_DoubleIsoEG22er2p1                         -> L1_DoubleLooseIsoEG22er2p1
            L1_IsoEG26er2p1_Jet34er3p0_dR_Min0p3          -> L1_LooseIsoEG26er2p1_Jet34er3p0_dR_Min0p3
            L1_IsoEG24er2p1_IsoTau27er2p1_dR_Min0p3       -> L1_LooseIsoEG24er2p1_IsoTau27er2p1_dR_Min0p3
            L1_DoubleIsoEG24er2p1                         -> L1_DoubleLooseIsoEG24er2p1
            L1_IsoEG22er2p1_IsoTau26er2p1_dR_Min0p3       -> L1_LooseIsoEG22er2p1_IsoTau26er2p1_dR_Min0p3
            L1_Mu5_IsoEG18                                -> L1_Mu5_LooseIsoEG18
            L1_IsoEG24er2p1_Jet26er3p0_dR_Min0p3          -> L1_LooseIsoEG24er2p1_Jet26er3p0_dR_Min0p3
            L1_IsoEG28er2p1_HTT100er                      -> L1_LooseIsoEG28er2p1_HTT100er
            
        replace
        =======
          https://its.cern.ch/jira/browse/CMSLITDPG-86
            -L1_ETT53_BptxAND
            -L1_ETT55_BptxAND
            -L1_ETT68_BptxAND
            +L1_ETT40_BptxAND
            +L1_ETT50_BptxAND
            +L1_ETT80_BptxAND
            +L1_ETT85_BptxAND
            +L1_ETT90_BptxAND
            +L1_ETT95_BptxAND
            +L1_ETT100_BptxAND
            +L1_ETT110_BptxAND
            
        scale
        =======
          https://its.cern.ch/jira/browse/CMSLITDPG-155
```
---
### L1Menu_Collisions2017_dev_r9 [2017-07-24]
---
  * [csv](https://github.com/cms-l1-dpg/2017-pp-menu-dev/blob/2017-07-24/Apr12/L1MenuId.csv)
  * [xml](https://raw.githubusercontent.com/cms-l1-dpg/2017-pp-menu-dev/2017-07-24/Apr12/L1Menu_Collisions2017_dev_r9.xml)
    * updates from L1Menu_Collisions2017_dev_r8
```
        add
        ===
          https://its.cern.ch/jira/browse/CMSLITDPG-156
            L1_DoubleJet150er3p0
          https://its.cern.ch/jira/browse/CMSLITDPG-158
            L1_DoubleEG8er2p6_HTT255er
            L1_DoubleEG8er2p6_HTT270er
            L1_DoubleEG8er2p6_HTT300er
          https://its.cern.ch/jira/browse/CMSLITDPG-159
            L1_HTT320er_QuadJet_70_55_40_40_er2p4
            L1_HTT320er_QuadJet_70_55_40_40_er2p5
            L1_HTT340er_QuadJet_70_55_40_40_er2p5
          https://its.cern.ch/jira/browse/CMSLITDPG-161
            L1_Mu20er2p1_IsoTau27er2p1
          https://its.cern.ch/jira/browse/CMSLITDPG-168
            L1_DoubleMuon_15_5_SQ
          https://its.cern.ch/jira/browse/CMSLITDPG-176
            L1_DoubleJet112er2p3_dEta_Max1p6
          https://its.cern.ch/jira/browse/CMSLITDPG-177
            L1_DoubleJet30_Mass_Min300_dEta_Max1p5
            L1_DoubleJet30_Mass_Min320_dEta_Max1p5
            L1_DoubleJet30_Mass_Min340_dEta_Max1p5
            L1_DoubleJet30_Mass_Min360_dEta_Max1p5
            L1_DoubleJet30_Mass_Min380_dEta_Max1p5
            L1_DoubleJet30_Mass_Min400_dEta_Max1p5
```

---
### L1Menu_Collisions2017_dev_r10 [2017-10-04]
---
  * [csv](https://github.com/cms-l1-dpg/2017-pp-menu-dev/blob/2017-10-04/Apr12/L1MenuId.csv)
  * [xml](https://raw.githubusercontent.com/cms-l1-dpg/2017-pp-menu-dev/2017-10-04/Apr12/L1Menu_Collisions2017_dev_r10.xml)
    * updates from L1Menu_Collisions2017_dev_r9
```
        add
        ===
          https://its.cern.ch/jira/browse/CMSLITDPG-237
            L1_DoubleMu5Upsilon_OS_DoubleEG3
            L1_DoubleMu3_OS_DoubleEG7p5Upsilon
            L1_TripleMu_5OQ_3p5OQ_2p5OQ_DoubleMu_5_2p5_OQ_OS_Mass_8to14
            L1_TripleMu_5OQ_3p5OQ_2p5OQ_DoubleMu_5_2p5_OQ_OS_Mass_5to17
          https://its.cern.ch/jira/browse/CMSLITDPG-269
            L1_HTT320er_QuadJet_70_55_45_45_er2p5
            L1_HTT340er_QuadJet_70_55_45_45_er2p5
          https://its.cern.ch/jira/browse/CMSLITDPG-264
            L1_TripleJet_98_83_71_VBF
            L1_TripleJet_100_85_72_VBF
            L1_TripleJet_105_85_76_VBF
          https://its.cern.ch/jira/browse/CMSLITDPG-221
            L1_DoubleMu0er2_SQ_dR_Max1p4
            L1_DoubleMu0er1p5_SQ_dR_Max1p4
            
        rename
        ======
          https://its.cern.ch/jira/browse/CMSLITDPG-281
            L1_DoubleJet40er3p0 -> L1_DoubleJet40er2p7
            L1_DoubleJet50er3p0 -> L1_DoubleJet50er2p7
            L1_DoubleJet60er3p0 -> L1_DoubleJet60er2p7
            L1_DoubleJet80er3p0 -> L1_DoubleJet80er2p7
            L1_DoubleJet100er3p0 -> L1_DoubleJet100er2p7
            L1_DoubleJet112er3p0 -> L1_DoubleJet112er2p7
            L1_DoubleJet120er3p0 -> L1_DoubleJet120er2p7
            L1_DoubleJet150er3p0 -> L1_DoubleJet150er2p7
            L1_QuadJet40er3p0 -> L1_QuadJet40er2p7
            L1_QuadJet50er3p0 -> L1_QuadJet50er2p7
            L1_QuadJet60er3p0 -> L1_QuadJet60er2p7
            L1_SingleJet20er3p0_NotBptxOR -> L1_SingleJet20er2p7_NotBptxOR
            L1_SingleJet20er3p0_NotBptxOR_3BX -> L1_SingleJet20er2p7_NotBptxOR_3BX
            L1_SingleJet43er3p0_NotBptxOR_3BX -> L1_SingleJet43er2p7_NotBptxOR_3BX
            L1_SingleJet46er3p0_NotBptxOR_3BX -> L1_SingleJet46er2p7_NotBptxOR_3BX
            L1_LooseIsoEG24er2p1_Jet26er3p0_dR_Min0p3 -> L1_LooseIsoEG24er2p1_Jet26er2p7_dR_Min0p3
            L1_LooseIsoEG26er2p1_Jet34er3p0_dR_Min0p3 -> L1_LooseIsoEG26er2p1_Jet34er2p7_dR_Min0p3
            L1_LooseIsoEG28er2p1_Jet34er3p0_dR_Min0p3 -> L1_LooseIsoEG28er2p1_Jet34er2p7_dR_Min0p3
            L1_LooseIsoEG30er2p1_Jet34er3p0_dR_Min0p3 -> L1_LooseIsoEG30er2p1_Jet34er2p7_dR_Min0p3
            L1_LooseIsoEG24er2p1_TripleJet_26er3p0_26_26er3p0 -> L1_LooseIsoEG24er2p1_TripleJet_26er2p7_26_26er2p7
            L1_Mu18_Jet24er3p0 -> L1_Mu18_Jet24er2p7
            L1_QuadJet36er3p0_Tau52 -> L1_QuadJet36er2p7_Tau52
            L1_QuadJet36er3p0_IsoTau52er2p1 -> L1_QuadJet36er2p7_IsoTau52er2p1
            L1_DoubleJet60er3p0_ETM60 -> L1_DoubleJet60er2p7_ETM60
            L1_DoubleJet60er3p0_ETM70 -> L1_DoubleJet60er2p7_ETM70
            L1_DoubleJet60er3p0_ETM80 -> L1_DoubleJet60er2p7_ETM80
            L1_DoubleJet60er3p0_ETM90 -> L1_DoubleJet60er2p7_ETM90
            L1_DoubleJet60er3p0_ETM100 -> L1_DoubleJet60er2p7_ETM100
            L1_Mu3_JetC16_dEta_Max0p4_dPhi_Max0p4 -> L1_Mu3_Jet16er2p7_dEta_Max0p4_dPhi_Max0p4
            L1_Mu3_JetC60_dEta_Max0p4_dPhi_Max0p4 -> L1_Mu3_Jet60er2p7_dEta_Max0p4_dPhi_Max0p4
            L1_Mu3_JetC120_dEta_Max0p4_dPhi_Max0p4 -> L1_Mu3_Jet120er2p7_dEta_Max0p4_dPhi_Max0p4
            
        remove
        ======
            https://its.cern.ch/jira/browse/CMSLITDPG-274
              L1_BPTX_AND_Ref2_NIM
              L1_BPTX_B1NotB2_NIM
              L1_BPTX_B2NotB1_NIM
              L1_BPTX_NotOR_NIM
              L1_BPTX_AND_NIM
              L1_BPTX_B1_NIM
              L1_BPTX_B2_NIM
              L1_BPTX_OR_NIM
            https://its.cern.ch/jira/browse/CMSLITDPG-303
              L1_CDC_3_TOP120_DPHI1p570_3p142
              L1_CDC_3_TOP120_DPHI2p094_3p142
              L1_CDC_3_TOP120_DPHI2p618_3p142
              L1_CDC_3_TOP_DPHI2p618_3p142
              L1_CDC_3_er1p2_TOP120_DPHI1p570_3p142
              L1_CDC_3_er1p2_TOP120_DPHI2p094_3p142
              L1_CDC_3_er1p2_TOP120_DPHI2p618_3p142
              L1_CDC_3_er1p6_TOP120_DPHI1p570_3p142
              L1_CDC_3_er1p6_TOP120_DPHI2p094_3p142
              L1_CDC_3_er1p6_TOP120_DPHI2p618_3p142
              L1_CDC_3_er2p1_TOP120_DPHI1p570_3p142
              L1_CDC_3_er2p1_TOP120_DPHI2p094_3p142
              L1_CDC_3_er2p1_TOP120_DPHI2p618_3p142
              L1_CDC_SingleMu_3_TOP120_DPHI2p618_3p142
              L1_CDC_SingleMu_3_er1p6_TOP120_DPHI2p618_3p142
              L1_CDC_SingleMu_3_er2p1_TOP120_DPHI2p618_3p142
              L1_CDCp1_3_TOP120_DPHI2p618_3p142
              L1_CDCp1_3_er1p2_TOP120_DPHI2p618_3p142
              L1_CDCp1_3_er1p6_TOP120_DPHI2p618_3p142
              L1_CDCp1_3_er2p1_TOP120_DPHI2p618_3p142
              L1_Jet32_DoubleMu_10_0_dPhi_Jet_Mu0_Max0p4_dPhi_Mu_Mu_Min1p0
              L1_Jet32_Mu0_EG10_dPhi_Jet_Mu_Max0p4_dPhi_Mu_EG_Min1p0
              L1_DoubleMu0_ETMHF40_Jet60_OR_DoubleJet30
              L1_DoubleMu0_ETMHF50_Jet60_OR_DoubleJet30
              L1_DoubleMu0_ETMHF60_Jet60_OR_DoubleJet30
              L1_DoubleMu0_ETMHF70_Jet60_OR_DoubleJet30
              L1_DoubleMu0_ETMHF80_Jet60_OR_DoubleJet30
              L1_ETMHF70_Jet60_OR_DoubleJet30
              L1_ETMHF75_Jet60_OR_DoubleJet30
              L1_ETMHF80_Jet60_OR_DoubleJet30
              L1_ETMHF85_Jet60_OR_DoubleJet30
              L1_ETMHF90_Jet60_OR_DoubleJet30
              L1_ETMHF95_Jet60_OR_DoubleJet30
              L1_ETMHF105_Jet60_OR_DoubleJet30
              L1_ETMHF110_Jet60_OR_DoubleJet30
              L1_ETMHF115_Jet60_OR_DoubleJet30
              L1_ETMHF120_Jet60_OR_DoubleJet30
              L1_ETMHF70_Jet60_OR_DiJet30woTT28
              L1_ETMHF80_Jet60_OR_DiJet30woTT28
              L1_ETMHF90_Jet60_OR_DiJet30woTT28
              L1_LooseIsoEG18er2p1_IsoTau24er2p1_dR_Min0p3
              L1_LooseIsoEG20er2p1_IsoTau25er2p1_dR_Min0p3
              L1_Mu16er2p1_Tau20er2p1
              L1_Mu16er2p1_Tau24er2p1
              L1_Mu18er2p1_Tau20er2p1
```
