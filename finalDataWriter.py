# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 20:58:28 2017

@author: Fernando Maletski

Merges the final dataset with the GeoJSON map information to be used by the HTML/D3.JS index.html
"""
import json

data = json.load(open('./data/finalData.json', 'rb'))

geo = json.load(open('./data/zones.geojson', 'rb'))

# main loop
for i in range(263):
    try:
        geo['features'][i]['data'] = data[str(i+1)]
    except:
        print(i+1) # used during prototyping to track missing data

# write final GeoJSON dataset
with open('./data/data.geojson', 'w') as f:
    json.dump(geo, f, separators=(',', ':'))
