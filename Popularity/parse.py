#!/usr/bin/env python

import sys,os,json

handle = open(sys.argv[1])
result = json.load(handle)

datasets = {}

for item in result["DATA"]:
    dataset = item["COLLNAME"]
    nacc = item["NACC"]
    if nacc not in datasets.keys(): datasets[nacc] = []
    datasets[nacc].append(dataset)
    
sorted_nacc = datasets.keys()
sorted_nacc.sort(reverse=True)

for nacc in sorted_nacc:
    array = datasets[nacc]
    array.sort
    for item in array:
        print item,nacc