#!/usr/bin/env python

import sys,getopt,urllib2,json,os,datetime,subprocess,shlex

requestIDs = None
details = False
try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["id=","details"])
except getopt.GetoptError:
    print 'Please specify comma separated list of PhEDEx request IDs with --id'
    sys.exit(2)

# check command line parameter
for opt, arg in opts :
    if opt == "--id" :
        requestIDs = arg.split(',')
    if opt == "--details" :
        details = True

if requestIDs == None:
    print 'Please specify comma separated list of PhEDEx request IDs with --id'
    sys.exit(2)
    
progress = {}

for requestID in requestIDs:
    url='https://cmsweb.cern.ch/phedex/datasvc/json/prod/subscriptions?create_since=365&request=' + str(requestID)
    jstr = urllib2.urlopen(url).read()
    jstr = jstr.replace("\n", " ")
    result = json.loads(jstr)
    for item in result['phedex']['dataset']:
        dataset = item['name']
        total = item['bytes']
        if dataset not in progress.keys(): progress[dataset] = {}
        progress[dataset]['total'] = total
        if 'nodes' not in progress[dataset].keys(): progress[dataset]['nodes'] = {}
        for subscription in item['subscription'] :
            node = subscription['node']
            current_bytes = subscription['node_bytes']
            if node not in progress[dataset]['nodes'].keys(): progress[dataset]['nodes'][node] = {}
            if 'current_bytes' not in progress[dataset]['nodes'][node].keys(): progress[dataset]['nodes'][node]['current_bytes'] = 0
            progress[dataset]['nodes'][node]['current_bytes'] += current_bytes
            
            
if details: print "\nDataset status for requests %s:\n" % ','.join(requestIDs)

progress_per_site = {}
for dataset in progress.keys():
    if details: print 'Dataset:',dataset
    for node in progress[dataset]['nodes']:
        if node not in progress_per_site.keys(): progress_per_site[node] = {}
        if 'total' not in progress_per_site[node].keys(): progress_per_site[node]['total'] = 0
        progress_per_site[node]['total'] += progress[dataset]['total']
        if 'current' not in progress_per_site[node].keys(): progress_per_site[node]['current'] = 0
        progress_per_site[node]['current'] += progress[dataset]['nodes'][node]['current_bytes']
        if details: print "%15s: %6.2f%% of %7.3f TB" % (node,float(progress[dataset]['nodes'][node]['current_bytes'])/float(progress[dataset]['total'])*100,float(progress[dataset]['total'])/1000000000000.)


print "\nOverall status for requests %s:\n" % ','.join(requestIDs)

for site in progress_per_site.keys():
    print "%15s: %6.2f%% of %7.3f TB" % (site,float(progress_per_site[site]['current'])/float(progress_per_site[site]['total'])*100,float(progress_per_site[site]['total'])/1000000000000.)
