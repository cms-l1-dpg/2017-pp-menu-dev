## L1 menu development
- [ ] Set deadline for request of seeds in sync with HLT menu
- [ ] Present the request at a meeting
  * [ ] prepare backup seeds for higher pileups
  * [ ] prepare monitoring seeds if needed
    * [ ] specify target rates for prescaled seeds
- [ ] All the approved requests should be entered in JIRA
  * https://its.cern.ch/jira/projects/CMSLITDPG/
    * adding/changing/removing L1 seeds
    * [ ] create a ticket in "L1TMenu" component
      * [ ] attach xml file including the proposed seeds
    * specifying target rates for monitoring seeds
      * [ ] create a ticket for  in "L1TMenuPrescaleSeeds" component
    * [ ] specify label for target HLT menu, e.g "HLTv3"
- [ ] Compile the seeds to create a full menu
  * [ ] Do not include any seeds which need new features not available in CMSSW release
- [ ] Perform offline test
- [ ] Check if the full menu can be synthesized to a working firmware
- [ ] Publish the full menu

## L1 menu deployment
- [ ] Perform offline O2O of the new menu for offline test of HLT with the target CMSSW release
- [ ] Check compatibility of CMSSW release on DQM/O2O machines
- [ ] Check compatibility of SWATCH cell
- [ ] Prepare prescale sets for the new menu
  * [ ] 2.2/2.0/1.8/1.6/1.4/1.2/0.75/0.5/0.25 x 10e34
- [ ] Preper configuration/run-setting keys for the new menu
