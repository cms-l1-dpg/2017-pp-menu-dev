# 2017-pp-menu-dev
Collection of development menus for 2017 proton collision

https://twiki.cern.ch/twiki/bin/viewauth/CMS/HowToL1TriggerMenu

Tutorial
https://indico.cern.ch/event/623817/

### initial collection of seeds
  * [csv](https://github.com/cms-l1-dpg/2017-pp-menu-dev/blob/version-1/Apr12/L1MenuId.csv)
  * [xml](https://raw.githubusercontent.com/cms-l1-dpg/2017-pp-menu-dev/version-1/Apr12/L1Menu_20170412.xml)
---
### L1Menu_Collisions2017_dev_r2 [2017-05-03-tsg]
  * [csv](https://github.com/cms-l1-dpg/2017-pp-menu-dev/blob/2017-05-03-tsg/Apr12/L1MenuId.csv)
  * [xml](https://raw.githubusercontent.com/cms-l1-dpg/2017-pp-menu-dev/2017-05-03-tsg/Apr12/L1Menu_Collisions2017_dev_r2.xml)
---
### L1Menu_Collisions2017_dev_r3 [2017-05-17]
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
  * [csv](https://github.com/cms-l1-dpg/2017-pp-menu-dev/blob/2017-06-26/Apr12/L1MenuId.csv)
  * [xml](https://raw.githubusercontent.com/cms-l1-dpg/2017-pp-menu-dev/2017-06-26/Apr12/L1Menu_Collisions2017_dev_r7.xml)
    * updates from L1Menu_Collisions2017_dev_r3 [2017-05-17] NB: compatible with L1Menu_Collisions2017_dev_r5_v3 deployed online 
      * https://its.cern.ch/jira/browse/CMSLITDPG-128
      * https://its.cern.ch/jira/browse/CMSLITDPG-113
      * https://its.cern.ch/jira/browse/CMSLITDPG-134
---
### L1Menu_Collisions2017_dev_r8 [2017-07-05]
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
