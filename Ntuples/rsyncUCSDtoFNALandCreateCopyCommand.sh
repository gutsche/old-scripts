#!/bin/bash
#
# execute in /storage/local/data2/cms1/cms2
# clean /pnfs/cms/WAX/resilient/gutsche
rsync -n -a -i --ignore-existing uaf-3.t2.ucsd.edu:/nfs-3/userdata/cms2/EG_Run2010A-Jul16thReReco-v2_RECO . | grep '.root' | awk '{print $2}'
rsync -n -a -i --ignore-existing uaf-3.t2.ucsd.edu:/nfs-3/userdata/cms2/EG_Run2010A-Jun14thReReco_v1_RECO . | grep '.root' | awk '{print $2}'
rsync -n -a -i --ignore-existing uaf-3.t2.ucsd.edu:/nfs-3/userdata/cms2/EG_Run2010A-PromptReco-v4_RECO . | grep '.root' | awk '{print $2}'
rsync -n -a -i --ignore-existing uaf-3.t2.ucsd.edu:/nfs-3/userdata/cms2/MinimumBias_Commissioning10-SD_EG-Jun14thSkim_v1_RECO . | grep '.root' | awk '{print $2}'
rsync -n -a -i --ignore-existing uaf-3.t2.ucsd.edu:/nfs-3/userdata/cms2/MinimumBias_Commissioning10-SD_Mu-Jun14thSkim_v1_RECO . | grep '.root' | awk '{print $2}'
rsync -n -a -i --ignore-existing uaf-3.t2.ucsd.edu:/nfs-3/userdata/cms2/Mu_Run2010A-Jul16thReReco-v1_RECO . | grep '.root' | awk '{print $2}'
rsync -n -a -i --ignore-existing uaf-3.t2.ucsd.edu:/nfs-3/userdata/cms2/Mu_Run2010A-Jun14thReReco_v1_RECO . | grep '.root' | awk '{print $2}'
rsync -n -a -i --ignore-existing uaf-3.t2.ucsd.edu:/nfs-3/userdata/cms2/Mu_Run2010A-PromptReco-v4_RECO . | grep '.root' | awk '{print $2}'
# rsync -n -a -i --ignore-existing uaf-3.t2.ucsd.edu:/data/tmp/cms2/ . | grep merge | awk '{print $2}' | awk '{print "lcg-cp -v -n 20 file:////`pwd`/"$1" srm://cmssrm.fnal.gov:8443/srm/managerv2?SFN=/resilient/gutsche/"$1}'
#rsync -n -a -i --ignore-existing uaf-3.t2.ucsd.edu:/nfs-3/userdata/cms2/ . | grep merge | awk '{print $2}' | awk '{print "lcg-cp -v -n 20 file:////`pwd`/"$1" srm://cmssrm.fnal.gov:8443/srm/managerv2?SFN=/resilient/gutsche/"$1}'
# copy output to uaf-3 and execute in /data/tmp/cms2
