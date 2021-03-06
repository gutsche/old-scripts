#!/usr/bin/env python

import sys, os, datetime, subprocess, shlex, tempfile, getopt, json

jsonfilename = None

opts, args = getopt.getopt(sys.argv[1:], "", ["json="])

for opt, arg in opts :
    if opt == "--json" :
        jsonfilename = arg
        
if jsonfilename == None :
    print ''
    print 'Please specify json filename with with run array with --json'
    print ''
    sys.exit(2)

recodatasets = [
'/DoubleElectron/Run2011A-PromptReco-v5/RECO',
'/DoubleMu/Run2011A-PromptReco-v5/RECO',
'/ElectronHad/Run2011A-PromptReco-v5/RECO',
'/HT/Run2011A-PromptReco-v5/RECO',
'/Jet/Run2011A-PromptReco-v5/RECO',
'/MET/Run2011A-PromptReco-v5/RECO',
'/MinimumBias/Run2011A-PromptReco-v5/RECO',
'/MuEG/Run2011A-PromptReco-v5/RECO',
'/MuHad/Run2011A-PromptReco-v5/RECO',
'/MuOnia/Run2011A-PromptReco-v5/RECO',
'/MultiJet/Run2011A-PromptReco-v5/RECO',
'/Photon/Run2011A-PromptReco-v5/RECO',
'/PhotonHad/Run2011A-PromptReco-v5/RECO',
'/SingleElectron/Run2011A-PromptReco-v5/RECO',
'/SingleMu/Run2011A-PromptReco-v5/RECO',
'/Tau/Run2011A-PromptReco-v5/RECO',
'/TauPlusX/Run2011A-PromptReco-v5/RECO',
'/BTag/Run2011A-PromptReco-v5/RECO',
'/ForwardTriggers/Run2011A-PromptReco-v5/RECO',
]

dpgskimdatasets = [
'/BTag/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/Commissioning/Run2011A-DT-PromptSkim-v5/RAW-RECO',
'/Commissioning/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/Commissioning/Run2011A-MuonDPG-PromptSkim-v5/RAW-RECO',
'/Cosmics/Run2011A-CosmicSP-PromptSkim-v5/RAW-RECO',
'/Cosmics/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/DoubleElectron/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/DoubleMu/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/ElectronHad/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/HT/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/Jet/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/MET/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/MinimumBias/Run2011A-BeamBkg-PromptSkim-v5/RAW-RECO',
'/MinimumBias/Run2011A-HSCPSD-PromptSkim-v5/RECO',
'/MinimumBias/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/MinimumBias/Run2011A-MuonTrack-PromptSkim-v5/RAW-RECO',
'/MinimumBias/Run2011A-ValSkim-PromptSkim-v5/RAW-RECO',
'/MuEG/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/MuHad/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/MuOnia/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/MultiJet/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/Photon/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/PhotonHad/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/SingleElectron/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/SingleMu/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/Tau/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
'/TauPlusX/Run2011A-LogError-PromptSkim-v5/RAW-RECO',
]

sdcsskimdatasets = [
'/BTag/Run2011A-EXOHSCP-PromptSkim-v5/USER',
'/DoubleElectron/Run2011A-HWW-PromptSkim-v5/AOD',
'/DoubleElectron/Run2011A-HZZ-PromptSkim-v5/AOD',
'/DoubleElectron/Run2011A-ZElectron-PromptSkim-v5/RAW-RECO',
'/DoubleMu/Run2011A-EXOHSCP-PromptSkim-v5/USER',
'/DoubleMu/Run2011A-HWW-PromptSkim-v5/AOD',
'/DoubleMu/Run2011A-HZZ-PromptSkim-v5/AOD',
'/DoubleMu/Run2011A-HighMET-PromptSkim-v5/RAW-RECO',
'/DoubleMu/Run2011A-WMu-PromptSkim-v5/RAW-RECO',
'/DoubleMu/Run2011A-ZMu-PromptSkim-v5/RAW-RECO',
'/HT/Run2011A-HighMET-PromptSkim-v5/RAW-RECO',
'/Jet/Run2011A-DiJet-PromptSkim-v5/USER',
'/Jet/Run2011A-HighMET-PromptSkim-v5/RAW-RECO',
'/MET/Run2011A-EXOHSCP-PromptSkim-v5/USER',
'/MET/Run2011A-HighMET-PromptSkim-v5/RAW-RECO',
'/MuEG/Run2011A-HWW-PromptSkim-v5/AOD',
'/MuEG/Run2011A-HZZ-PromptSkim-v5/AOD',
'/Photon/Run2011A-DiPhoton-PromptSkim-v5/RAW-RECO',
'/Photon/Run2011A-DoublePhoton-PromptSkim-v5/AOD',
'/Photon/Run2011A-HighMET-PromptSkim-v5/RAW-RECO',
'/Photon/Run2011A-WElectron-PromptSkim-v5/RAW-RECO',
'/Photon/Run2011A-ZElectron-PromptSkim-v5/RAW-RECO',
'/SingleElectron/Run2011A-HWW-PromptSkim-v5/AOD',
'/SingleElectron/Run2011A-HZZ-PromptSkim-v5/AOD',
'/SingleElectron/Run2011A-HighMET-PromptSkim-v5/RAW-RECO',
'/SingleElectron/Run2011A-Tau-PromptSkim-v5/RAW-RECO',
'/SingleElectron/Run2011A-WElectron-PromptSkim-v5/RAW-RECO',
'/SingleMu/Run2011A-EXOHSCP-PromptSkim-v5/USER',
'/SingleMu/Run2011A-HWW-PromptSkim-v5/AOD',
'/SingleMu/Run2011A-HZZ-PromptSkim-v5/AOD',
'/SingleMu/Run2011A-HighMET-PromptSkim-v5/RAW-RECO',
'/SingleMu/Run2011A-Tau-PromptSkim-v5/RAW-RECO',
'/SingleMu/Run2011A-WMu-PromptSkim-v5/RAW-RECO',
'/SingleMu/Run2011A-ZMu-PromptSkim-v5/RAW-RECO',
]

def queryForSize(run,datasets):

    result = {}
    
    for dataset in datasets :
    
        commandline = "dbs search --query=\"find run,sum(block.size) where run = " + str(run) + " and dataset = " + dataset + "\" --noheader"
        args = shlex.split(commandline)
        output = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE)
        output_array = output.communicate()[0].split('\n')
    
        if len(output_array) >= 1 :
            array = output_array[0].split()
            if len(array) == 2 :
                tmprun = int(array[0])
                size = float(array[1])/1024./1024./1024.
                if tmprun in result.keys() :
                    result[tmprun] += size 
                else :
                    result[tmprun] = size
    
    if run in result.keys():
        print 'Query for run',run,'resulted in:',result[run]
        return result[run]
    else :
        print 'Query for run',run,'resulted in: 0.'
        return 0.


runs = json.load(open(jsonfilename))
sorted_runs = runs
sorted_runs.sort()
all_runs = sorted_runs

if len(all_runs) == 0 :
    print ''
    print 'No runs included in json file'
    print ''
    sys.exit(1)

print ''
print 'Query for reco datasets'
print ''
recodatasets_result = {}
for run in all_runs : 
    recodatasets_result[run] = queryForSize(run,recodatasets)

print ''
print 'Query for dpg skims'
print ''
dpgskimdatasets_result = {}
for run in all_runs : 
    dpgskimdatasets_result[run] = queryForSize(run,dpgskimdatasets)

print ''
print 'Query for SD/CS skims'
print ''
sdcsskimdatasets_result = {}
for run in all_runs : 
    sdcsskimdatasets_result[run] = queryForSize(run,sdcsskimdatasets)
    
for run in all_runs:
    if recodatasets_result[run] > 0. :
        dpgpercentage = (dpgskimdatasets_result[run])/recodatasets_result[run]*100.
        sdscpercentage = (sdcsskimdatasets_result[run])/recodatasets_result[run]*100.
        percentage = (dpgskimdatasets_result[run] + sdcsskimdatasets_result[run])/recodatasets_result[run]*100.
        print run,recodatasets_result[run],dpgskimdatasets_result[run],sdcsskimdatasets_result[run],dpgpercentage,sdscpercentage,percentage
