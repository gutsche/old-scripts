cat all_accessed_datasets.list | grep Summer11 | grep PU_S4 | grep AODSIM > summer11_all_accessed_aodsim.list
cat summer11_all_accessed_aodsim.list | awk '{print $1}' | sort > summer11_all_accessed_aodsim_sorted.list
dbs --query="find dataset where dataset.status=VALID and dataset = *Summer11*PU_S4*AODSIM" > summer11_all_aodsim.list
cat summer11_all_aodsim.list | sort > summer11_all_aodsim_sorted.list
comm -13 summer11_all_accessed_aodsim_sorted.list summer11_all_aodsim_sorted.list > summer11_not_accessed_aodsim.list

cat all_accessed_datasets.list | grep Fall11 | grep AODSIM | grep PU_S6 | grep START44_V9 > fall11_44X_all_accessed_aodsim.list
cat fall11_44X_all_accessed_aodsim.list | awk '{print $1}' | sort > fall11_44X_all_accessed_aodsim_sorted.list
dbs --query="find dataset where dataset.status=VALID and dataset = *Fall11*PU_S6*START44_V9*AODSIM" > fall11_44X_all_aodsim.list
cat fall11_44X_all_aodsim.list | sort > fall11_44X_all_aodsim_sorted.list
comm -13 fall11_44X_all_accessed_aodsim_sorted.list fall11_44X_all_aodsim_sorted.list > fall11_44X_not_accessed_aodsim.list

cat all_accessed_datasets.list | grep Fall11 | grep AODSIM | grep PU_S6 | grep START42 > fall11_42X_all_accessed_aodsim.list
cat fall11_42X_all_accessed_aodsim.list | awk '{print $1}' | sort > fall11_42X_all_accessed_aodsim_sorted.list
dbs --query="find dataset where dataset.status=VALID and dataset = *Fall11*PU_S6*START42*AODSIM" > fall11_42X_all_aodsim.list
cat fall11_42X_all_aodsim.list | sort > fall11_42X_all_aodsim_sorted.list
comm -13 fall11_42X_all_accessed_aodsim_sorted.list fall11_42X_all_aodsim_sorted.list > fall11_42X_not_accessed_aodsim.list

cat all_accessed_datasets.list | grep Summer11 | grep PU_S4 | grep GEN-SIM-RECO > summer11_all_accessed_reco.list
cat summer11_all_accessed_reco.list | awk '{print $1}' | sort > summer11_all_accessed_reco_sorted.list
dbs --query="find dataset where dataset.status=VALID and dataset = *Summer11*PU_S4*GEN-SIM-RECO" > summer11_all_reco.list
cat summer11_all_reco.list | sort > summer11_all_reco_sorted.list
comm -13 summer11_all_accessed_reco_sorted.list summer11_all_reco_sorted.list > summer11_not_accessed_reco.list

cat all_accessed_datasets.list | grep Fall11 | grep GEN-SIM- | grep PU_S6 | grep START44_V9 > fall11_44X_all_accessed_reco.list
cat fall11_44X_all_accessed_reco.list | awk '{print $1}' | sort > fall11_44X_all_accessed_reco_sorted.list
dbs --query="find dataset where dataset.status=VALID and dataset = *Fall11*PU_S6*START44_V9*GEN-SIM-RECO" > fall11_44X_all_reco.list
cat fall11_44X_all_reco.list | sort > fall11_44X_all_reco_sorted.list
comm -13 fall11_44X_all_accessed_reco_sorted.list fall11_44X_all_reco_sorted.list > fall11_44X_not_accessed_reco.list

cat all_accessed_datasets.list | grep Fall11 | grep GEN-SIM-RECO | grep PU_S6 | grep START42 > fall11_42X_all_accessed_reco.list
cat fall11_42X_all_accessed_reco.list | awk '{print $1}' | sort > fall11_42X_all_accessed_reco_sorted.list
dbs --query="find dataset where dataset.status=VALID and dataset = *Fall11*PU_S6*START42*GEN-SIM-RECO" > fall11_42X_all_reco.list
cat fall11_42X_all_reco.list | sort > fall11_42X_all_reco_sorted.list
comm -13 fall11_42X_all_accessed_reco_sorted.list fall11_42X_all_reco_sorted.list > fall11_42X_not_accessed_reco.list

