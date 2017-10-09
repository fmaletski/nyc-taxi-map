# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 20:58:28 2017

@author: Fernando Maletski
"""
import json

data = json.load(open('finalData.json', 'rb'))

geo = json.load(open('zones.geojson', 'rb'))

for i in range(263):
    try:
        geo['features'][i]['data'] = data[str(i+1)]
    except: print(i+1)
    
with open('data.geojson', 'w') as f:
    json.dump(geo, f, separators=(',', ':'))
