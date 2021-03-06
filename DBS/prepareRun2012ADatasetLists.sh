python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2012A*/*" | grep -v 'test/' | sort > complete_datasets.list

cat complete_datasets.list | grep -i express > express.list
cat complete_datasets.list | grep -i preprod > preproduction.list
cat complete_datasets.list | grep -- '-Error' > error.list

cat complete_datasets.list | grep -vi express | grep -vi preprod | grep -v -- '-Error' > datasets.list

cat datasets.list | grep '/RAW' | grep -v RAW-RECO | grep v1 > raw_v1.list

cat datasets.list | grep '/RECO' | grep -i prompt | grep v1 > prompt_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i prompt | grep v1 > prompt_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i prompt | grep v1 > prompt_dqm_v1.list
cat datasets.list | grep -i promptskim | grep v1 > prompt_skim_v1.list
cat datasets.list | grep ALCA | grep v1 > alcareco_v1.list
# prompt_reco_v1.list prompt_aod_v1.list prompt_dqm_v1.list alcareco_v1.list prompt_skim_v1.list

cat datasets.list | grep '/RECO' | grep -i 15Apr2012 | grep v1 > 15Apr2012_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 15Apr2012 | grep v1 > 15Apr2012_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 15Apr2012 | grep v1 > 15Apr2012_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 15Apr2012 | grep v1 > 15Apr2012_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 15Apr2012 | grep v1 > 15Apr2012_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 15Apr2012 | grep v1 >> 15Apr2012_skims_v1.list
# 15Apr2012_reco_v1.list 15Apr2012_aod_v1.list 15Apr2012_dqm_v1.list 15Apr2012_alcareco_v1.list 15Apr2012_skims_v1.list 15Apr2012_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 26Apr2012 | grep v1 > 26Apr2012_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 26Apr2012 | grep v1 > 26Apr2012_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 26Apr2012 | grep v1 > 26Apr2012_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 26Apr2012 | grep v1 > 26Apr2012_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 26Apr2012 | grep v1 > 26Apr2012_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 26Apr2012 | grep v1 >> 26Apr2012_skims_v1.list
# 26Apr2012_reco_v1.list 26Apr2012_aod_v1.list 26Apr2012_dqm_v1.list 26Apr2012_alcareco_v1.list 26Apr2012_skims_v1.list 26Apr2012_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 26Apr2012 | grep v2 > 26Apr2012_reco_v2.list
cat datasets.list | grep '/AOD' | grep -i 26Apr2012 | grep v2 > 26Apr2012_aod_v2.list
cat datasets.list | grep '/DQM' | grep -i 26Apr2012 | grep v2 > 26Apr2012_dqm_v2.list
cat datasets.list | grep '/ALCARECO' | grep -i 26Apr2012 | grep v2 > 26Apr2012_alcareco_v2.list
cat datasets.list | grep '/RAW-RECO' | grep -i 26Apr2012 | grep v2 > 26Apr2012_skims_v2.list
cat datasets.list | grep '/USER' | grep -i 26Apr2012 | grep v2 >> 26Apr2012_skims_v2.list
# 26Apr2012_reco_v2.list 26Apr2012_aod_v2.list 26Apr2012_dqm_v2.list 26Apr2012_alcareco_v2.list 26Apr2012_skims_v2.list 26Apr2012_skims_v2.list


# cat datasets.list | grep '/RECO' | grep -i 14Oct2011 | grep v1 > 14Oct2011_reco_v1.list
# cat datasets.list | grep '/AOD' | grep -i 14Oct2011 | grep v1 > 14Oct2011_aod_v1.list
# cat datasets.list | grep '/DQM' | grep -i 14Oct2011 | grep v1 > 14Oct2011_dqm_v1.list
# cat datasets.list | grep '/ALCARECO' | grep -i 14Oct2011 | grep v1 > 14Oct2011_alcareco_v1.list
# cat datasets.list | grep '/RAW-RECO' | grep -i 14Oct2011 | grep v1 > 14Oct2011_skims_v1.list
# cat datasets.list | grep '/USER' | grep -i 14Oct2011 | grep v1 >> 14Oct2011_skims_v1.list
# 14Oct2011_reco_v1.list 14Oct2011_aod_v1.list 14Oct2011_dqm_v1.list 14Oct2011_alcareco_v1.list 14Oct2011_skims_v1.list 14Oct2011_skims_v1.list

cat express.list error.list preproduction.list raw_v1.list prompt_reco_v1.list prompt_aod_v1.list prompt_dqm_v1.list alcareco_v1.list prompt_skim_v1.list 15Apr2012_reco_v1.list 15Apr2012_aod_v1.list 15Apr2012_dqm_v1.list 15Apr2012_alcareco_v1.list 15Apr2012_skims_v1.list 15Apr2012_skims_v1.list 26Apr2012_reco_v1.list 26Apr2012_aod_v1.list 26Apr2012_dqm_v1.list 26Apr2012_alcareco_v1.list 26Apr2012_skims_v1.list 26Apr2012_skims_v1.list 26Apr2012_reco_v2.list 26Apr2012_aod_v2.list 26Apr2012_dqm_v2.list 26Apr2012_alcareco_v2.list 26Apr2012_skims_v2.list 26Apr2012_skims_v2.list | sort > done.list

echo ""
echo "inconsistencies"
echo ""
diff datasets.list done.list | grep '<' | awk '{print $2}'

echo ""
echo "Error datasets"
echo ""
cat error.list

echo ""
echo "PDs missing in FNAL checks"
echo ""
cat datasets.list | grep -v '/AlCaP0/' | grep -v '/AlCaPhiSym/' | grep -v '/BTag/' | grep -v '/DoubleMu/' | grep -v '/ElectronHad/' | grep -v '/ForwardTriggers/' | grep -v '/HT/' | grep -v '/HcalNZS/' | grep -v '/HcalHPDNoise/' | grep -v '/MET/' | grep -v '/MinimumBias/' | grep -v '/MuHad/' | grep -v '/MuOnia/' | grep -v '/ZeroBias1/' | grep -v '/ZeroBias2/' | grep -v '/ZeroBias3/' | grep -v '/ZeroBias4/' | grep -v '/Commissioning/' | grep -v '/Cosmics/' | grep -v '/DoubleElectron/' | grep -v '/Jet/' | grep -v '/MuEG/' | grep -v '/MultiJet/' | grep -v '/Photon/' | grep -v '/PhotonHad/' | grep -v '/SingleElectron/' | grep -v '/SingleMu/' | grep -v '/Tau/' | grep -v '/TauPlusX/' | grep -v '/AlCaLumiPixels/' | grep -v '/FEDMonitor/' | grep -v '/L1Accept/' | grep -v '/LogMonitor/' | grep -v '/MiniDaq/' | grep -v '/RPCMonitor/' | grep -v '/TestEnablesEcalHcalDT/' | grep -v '/TestEnablesTracker/' | grep -v '/LP_Central/' | grep -v '/LP_Forward/' | grep -v '/LP_L1Jets/' | grep -v '/LP_MinBias1/' | grep -v '/LP_MinBias2/' | grep -v '/LP_ZeroBias/' | grep -v '/DoubleMuParked/' | awk -F\/ '{print $2}' | sort | uniq
echo ""
echo "datasets not at FNAL"
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2012A*/* and site = T1_US_FNAL" | grep -v 'test/' | sort > datasets_fnal.list
echo ""
echo "PDs staying at CERN: AlCaLumiPixels, FEDMonitor, L1Accept, LogMonitor, MiniDaq, RPCMonitor, TestEnablesEcalHcalDT, TestEnablesTracker"
echo ""
echo "PDs not going non-custodially to FNAL: DoubleMuParked"
echo ""
echo "FNAL custodial for: AlCaP0, AlCaPhiSym, BTag, DoubleMu, ElectronHad, ForwardTriggers, HT, HcalNZS, HcalHPDNoise, LP_Central, LP_Forward, LP_L1Jets, LP_MinBias1, LP_MinBias2, LP_ZeroBias, MET, MinimumBias, MuHad, MuOnia, ZeroBias1, ZeroBias2, ZeroBias3, ZeroBias4"
echo ""
echo "missing:"
diff datasets.list datasets_fnal.list | grep '/AlCaP0/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/AlCaPhiSym/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/BTag/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/DoubleMu/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ElectronHad/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ForwardTriggers/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/HT/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/HcalNZS/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/HcalHPDNoise/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/LP_Central/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/LP_Forward/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/LP_L1Jets/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/LP_MinBias1/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/LP_MinBias2/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/LP_ZeroBias/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MET/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MinimumBias/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MuHad/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MuOnia/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ZeroBias1/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ZeroBias2/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ZeroBias3/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ZeroBias4/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
echo ""
echo "non-custodial kept at FNAL for Commissioning, Cosmics, DoubleElectron, Jet, MuEG, MultiJet, Photon, PhotonHad, SingleElectron, SingleMu, Tau, TauPlusX"
echo ""
echo "missing:"
diff datasets.list datasets_fnal.list | grep '/Commissioning/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Cosmics/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/DoubleElectron/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Jet/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MuEG/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MultiJet/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Photon/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/PhotonHad/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/SingleElectron/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/SingleMu/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Tau/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/TauPlusX/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
echo ""