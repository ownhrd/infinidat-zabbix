#!/usr/bin/env python
__author__ = "Igor Sidorenko"
__email__ = "neither89@gmail.com"
__status__ = "Production"

import json
import sys, requests, time, os, urllib3
from datetime import datetime
from requests.auth import HTTPBasicAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
login = ''
password = ''

# lld for Zabbix
if len(sys.argv) == 3:
    ip = str(sys.argv[1])
    item = str(sys.argv[2])
    r = requests.get('https://'+ip+'/api/rest/'+item+'/', auth=HTTPBasicAuth(login,password), verify=False)
    data = r.json()
    jdata = []

# Get all Service Status
    if item == "services":
        for id in data['result']:
            jdata.append({"{#NAME}":id['name']})
        print(json.dumps({"data":jdata}))

# Else
    else:
        for id in data['result']:
            jdata.append({"{#NAME}":id['name'], "{#ID}": id['id']})
        print(json.dumps({"data":jdata}))

# System performance metrics
elif len(sys.argv) == 4:
    ip = str(sys.argv[1])
    item = str(sys.argv[2])
    key = str(sys.argv[3])
    if item == "system":
        r = requests.get('https://'+ip+'/api/rest/counters/'+item+'/total/', auth=HTTPBasicAuth(login,password), verify=False)
        data = r.json()
        print (data['result'][key])

# State, space, capacityy, enclosures
elif len(sys.argv) == 5:
    ip = str(sys.argv[1])
    item = str(sys.argv[2])
    itemid = str(sys.argv[3])
    key = str(sys.argv[4])

    if item == "pools" or item == "volumes" or item == "filesystems":
        r = requests.get('https://'+ip+'/api/rest/'+item+'/'+itemid+'/', auth=HTTPBasicAuth(login,password), verify=False)
        data = r.json()
        print (data['result'][key])

# Get enclosures ID
    elif item == "racks" and key == "enclosures":
        r = requests.get('https://'+ip+'/api/rest/components/'+item+'/'+itemid+'/'+key+'/', auth=HTTPBasicAuth(login,password), verify=False)
        data = r.json()
        jdata = []
        for id in data['result']:
            jdata.append({"{#ID}": id['id']})
        print(json.dumps({"data":jdata}))

# Get the Rack Nodes
    elif item == "racks" and key == "nodes":
        r = requests.get('https://'+ip+'/api/rest/components/'+item+'/'+itemid+'/'+key+'/', auth=HTTPBasicAuth(login,password), verify=False)
        data = r.json()
        jdata = []
        for id in data['result']:
            jdata.append({"{#ID}": id['id']})
        print(json.dumps({"data":jdata}))

# Get all Upss
    elif item == "racks" and key == "ups":
        r = requests.get('https://'+ip+'/api/rest/components/'+item+'/'+itemid+'/'+key+'/', auth=HTTPBasicAuth(login,password), verify=False)
        data = r.json()
        jdata = []
        for id in data['result']:
            jdata.append({"{#ID}": id['id']})
        print(json.dumps({"data":jdata}))

# Get Service Status
    elif item == "services":
        r = requests.get('https://'+ip+'/api/rest/'+item+'/'+itemid+'/', auth=HTTPBasicAuth(login,password), verify=False)
        data = r.json()
        print (data['result'][key])

# Perfomance metrics
elif len(sys.argv) == 6:
    ip = str(sys.argv[1])
    counter = str(sys.argv[2])
    item = str(sys.argv[3])
    itemid = str(sys.argv[4])
    key = str(sys.argv[5])

# Get Host Counters Total
    if counter == "counters" and item == "hosts":
        r = requests.get('https://'+ip+'/api/rest/counters/'+item+'/'+itemid+'/total/', auth=HTTPBasicAuth(login,password), verify=False)
        data = r.json()
        print (data['result'][key])

# Get Total IO Counters for a Volume
    if counter == "counters" and item == "volumes":
        r = requests.get('https://'+ip+'/api/rest/counters/'+item+'/'+itemid+'/total/', auth=HTTPBasicAuth(login,password), verify=False)
        data = r.json()
        print (data['result'][key])

elif len(sys.argv) == 7:
    ip = str(sys.argv[1])
    component = str(sys.argv[2])
    rack= str(sys.argv[3])
    item = str(sys.argv[4])
    itemid = str(sys.argv[5])
    key = str(sys.argv[6])

# Get Enclosure by ID
    if component == "racks" and item == "enclosures":
        r = requests.get('https://'+ip+'/api/rest/components/'+component+'/'+rack+'/'+item+'/'+itemid+'', auth=HTTPBasicAuth(login,password), verify=False)
        data = r.json()
        if key == "power_supplies1":
            for id in data['result']['power_supplies']:
                if id['id'] == 1:
                    print (id['state'])

        elif key == "power_supplies2":
            for id in data['result']['power_supplies']:
                if id['id'] == 2:
                    print (id['state'])

        elif key != "power_supplies2" and key != "power_supplies2":
            print (data['result'][key])

# Get Rack Node by ID
    if component == "racks" and item == "nodes":
        r = requests.get('https://'+ip+'/api/rest/components/'+component+'/'+rack+'/'+item+'/'+itemid+'', auth=HTTPBasicAuth(login,password), verify=False)
        data = r.json()
        if key == "power_supplies1":
            for id in data['result']['power_supplies']:
                if id['id'] == 1:
                    print (id['state'])

        elif key == "power_supplies2":
            for id in data['result']['power_supplies']:
                if id['id'] == 2:
                    print (id['state'])

        elif key != "power_supplies2" and key != "power_supplies2":
            print (data['result'][key])

# Get Ups by ID
    if component == "racks" and item == "ups":
        r = requests.get('https://'+ip+'/api/rest/components/'+component+'/'+rack+'/'+item+'/'+itemid+'', auth=HTTPBasicAuth(login,password), verify=False)
        data = r.json()
        print (data['result'][key])
