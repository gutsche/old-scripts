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
'/DoubleElectron/Run2011A-PromptReco-v4/RECO',
'/DoubleMu/Run2011A-PromptReco-v4/RECO',
'/ElectronHad/Run2011A-PromptReco-v4/RECO',
'/HT/Run2011A-PromptReco-v4/RECO',
'/Jet/Run2011A-PromptReco-v4/RECO',
'/MET/Run2011A-PromptReco-v4/RECO',
'/MinimumBias/Run2011A-PromptReco-v4/RECO',
'/MuEG/Run2011A-PromptReco-v4/RECO',
'/MuHad/Run2011A-PromptReco-v4/RECO',
'/MuOnia/Run2011A-PromptReco-v4/RECO',
'/MultiJet/Run2011A-PromptReco-v4/RECO',
'/Photon/Run2011A-PromptReco-v4/RECO',
'/PhotonHad/Run2011A-PromptReco-v4/RECO',
'/SingleElectron/Run2011A-PromptReco-v4/RECO',
'/SingleMu/Run2011A-PromptReco-v4/RECO',
'/Tau/Run2011A-PromptReco-v4/RECO',
'/TauPlusX/Run2011A-PromptReco-v4/RECO',
'/BTag/Run2011A-PromptReco-v4/RECO',
'/ForwardTriggers/Run2011A-PromptReco-v4/RECO',
]

dpgskimdatasets = [
'/BTag/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/Commissioning/Run2011A-DT-PromptSkim-v4/RAW-RECO',
'/Commissioning/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/Commissioning/Run2011A-MuonDPG-PromptSkim-v4/RAW-RECO',
'/Cosmics/Run2011A-CosmicSP-PromptSkim-v4/RAW-RECO',
'/Cosmics/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/DoubleElectron/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/DoubleMu/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/ElectronHad/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/HT/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/Jet/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/MET/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/MinimumBias/Run2011A-BeamBkg-PromptSkim-v4/RAW-RECO',
'/MinimumBias/Run2011A-HSCPSD-PromptSkim-v4/RECO',
'/MinimumBias/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/MinimumBias/Run2011A-MuonTrack-PromptSkim-v4/RAW-RECO',
'/MinimumBias/Run2011A-ValSkim-PromptSkim-v4/RAW-RECO',
'/MuEG/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/MuHad/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/MuOnia/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/MultiJet/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/Photon/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/PhotonHad/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/SingleElectron/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/SingleMu/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/Tau/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
'/TauPlusX/Run2011A-LogError-PromptSkim-v4/RAW-RECO',
]

sdcsskimdatasets = [
'/BTag/Run2011A-EXOHSCP-PromptSkim-v4/USER',
'/DoubleElectron/Run2011A-HWW-PromptSkim-v4/AOD',
'/DoubleElectron/Run2011A-HZZ-PromptSkim-v4/AOD',
'/DoubleElectron/Run2011A-ZElectron-PromptSkim-v4/RAW-RECO',
'/DoubleMu/Run2011A-EXOHSCP-PromptSkim-v4/USER',
'/DoubleMu/Run2011A-HWW-PromptSkim-v4/AOD',
'/DoubleMu/Run2011A-HZZ-PromptSkim-v4/AOD',
'/DoubleMu/Run2011A-HighMET-PromptSkim-v4/RAW-RECO',
'/DoubleMu/Run2011A-WMu-PromptSkim-v4/RAW-RECO',
'/DoubleMu/Run2011A-ZMu-PromptSkim-v4/RAW-RECO',
'/HT/Run2011A-HighMET-PromptSkim-v4/RAW-RECO',
'/Jet/Run2011A-DiJet-PromptSkim-v4/USER',
'/Jet/Run2011A-HighMET-PromptSkim-v4/RAW-RECO',
'/MET/Run2011A-EXOHSCP-PromptSkim-v4/USER',
'/MET/Run2011A-HighMET-PromptSkim-v4/RAW-RECO',
'/MuEG/Run2011A-HWW-PromptSkim-v4/AOD',
'/MuEG/Run2011A-HZZ-PromptSkim-v4/AOD',
'/Photon/Run2011A-DiPhoton-PromptSkim-v4/RAW-RECO',
'/Photon/Run2011A-DoublePhoton-PromptSkim-v4/AOD',
'/Photon/Run2011A-HighMET-PromptSkim-v4/RAW-RECO',
'/Photon/Run2011A-WElectron-PromptSkim-v4/RAW-RECO',
'/Photon/Run2011A-ZElectron-PromptSkim-v4/RAW-RECO',
'/SingleElectron/Run2011A-HWW-PromptSkim-v4/AOD',
'/SingleElectron/Run2011A-HZZ-PromptSkim-v4/AOD',
'/SingleElectron/Run2011A-HighMET-PromptSkim-v4/RAW-RECO',
'/SingleElectron/Run2011A-Tau-PromptSkim-v4/RAW-RECO',
'/SingleElectron/Run2011A-WElectron-PromptSkim-v4/RAW-RECO',
'/SingleMu/Run2011A-EXOHSCP-PromptSkim-v4/USER',
'/SingleMu/Run2011A-HWW-PromptSkim-v4/AOD',
'/SingleMu/Run2011A-HZZ-PromptSkim-v4/AOD',
'/SingleMu/Run2011A-HighMET-PromptSkim-v4/RAW-RECO',
'/SingleMu/Run2011A-Tau-PromptSkim-v4/RAW-RECO',
'/SingleMu/Run2011A-WMu-PromptSkim-v4/RAW-RECO',
'/SingleMu/Run2011A-ZMu-PromptSkim-v4/RAW-RECO',
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
