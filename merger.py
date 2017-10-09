# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:27:21 2017

@author: Fernando Maletski
"""

import pandas as pd
import numpy as np
import time
import json

frames = []

for i in range(10):
    frames.append(pd.read_csv('parsed{}.csv'.format(i)))

data = pd.concat(frames)
data.drop('Unnamed: 0', inplace = True, axis=1)
#data.to_csv('parsed.csv')

#locid = pd.read_csv('locid.csv')

def filterValues(data, field):
    values = np.append('all', data[field].unique())
    return values

zones = range(1,264)
weekends = filterValues(data, 'weekend')
times_of_day = filterValues(data, 'time_of_day')

def query(data, mode, zone, weekend, time_of_day):
    if weekend == 'all':
        weekend = ''
    else:
        weekend = " and weekend == '{}'".format(weekend)
    if time_of_day == 'all':
        time_of_day = ''
    else:
        time_of_day = " and time_of_day == '{}'".format(time_of_day)
    
    rows = data.query("{} == {}{}{}".format(mode, zone, 
                                                  weekend, time_of_day)) 
    count = np.sum(rows['count'])
    price = round(np.sum(rows['price']*rows['count']/count), 2)
    result = {'count': count,
              'price': price}

    return result

start = time.time()
total = 263*len(weekends)*len(times_of_day) 
finalData = {}
for zone in zones:
    finalData.update({str(zone): {}})
    originDict = finalData[str(zone)]
    for weekend in weekends:
        originDict.update({weekend: {}})
        weekDict = originDict[weekend]
        for time_of_day in times_of_day:
            dataPoint = {'origin': query(data, 'origin', zone, weekend, 
                                     time_of_day),
                         'destination': query(data, 'destination', zone, weekend, 
                                     time_of_day)
                         }
            weekDict.update({time_of_day: dataPoint})
            if i%250 == 0: print(round(time.time()-start, 2), ': ', 
                                 round(i*100/total, 2), ' %')
            i += 1

with open('finalData.json', 'w') as f:
    json.dump(finalData, f, separators=(',', ':'))
