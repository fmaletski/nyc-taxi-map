# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:36:20 2017

@author: Fernando Maletski
"""

import pandas as pd
import time
import sys

start = time.time()
print('importing: ', time.time()-start)
data = pd.read_csv('yellow_tripdata_2017-06.csv')
locid = pd.read_csv('locid.csv')

columns_to_drop = ['VendorID', 'tpep_dropoff_datetime', 'store_and_fwd_flag',
                   'RatecodeID', 'passenger_count', 'trip_distance',
                   'fare_amount', 'extra', 'mta_tax', 'tolls_amount',
                   'improvement_surcharge', 'payment_type']

data.drop(columns_to_drop, inplace=True, axis=1)

print('imported: ', time.time()-start)

def locations_zone(x):
    if x == 264 or x == 265:
        return 'Out of NYC'
    else:
        return locid.loc[x-1]['Zone']
 
def weekend(x):
    if x.weekday() >= 5:
        return 'weekend'
    else:
        return 'weekday'
    
def time_of_day(x):
    hour = x.hour
    if hour >= 5 and hour < 12:
        return 'morning'
    if hour >= 12 and hour < 18:
        return 'afternoon'
    if hour >= 18 and hour < 22:
        return 'evening'
    else:
        return 'night'

data['origin'] = data['PULocationID']
data['destination'] = data['DOLocationID']
data['price'] = data['total_amount'] - data['tip_amount']
data['datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])
data['weekend'] = data['datetime'].apply(weekend)
data['time_of_day'] = data['datetime'].apply(time_of_day)

columns_to_drop2 = ['tpep_pickup_datetime', 'PULocationID', 'DOLocationID',
                    'tip_amount', 'total_amount', 'datetime']

data.drop(columns_to_drop2, inplace=True, axis=1)

print('parsed: ', time.time()-start)

weekend = data['weekend'].unique()
time_of_day = data['time_of_day'].unique()
origins = data['origin'].unique()
destinations = data['destination'].unique()


filters = []
index = 0
for day in weekend:
    for time_ in time_of_day:
        for origin in origins:
            for destination in destinations:
                filters.append([index , "weekend == '{}' and time_of_day == '{}' and origin == '{}' and destination == '{}'".format(day,
                                   time_, origin, destination), day,
                                   time_, origin, destination])
                index += 1


interval = len(filters)//10
intervalList = []
for x in range(10):
    intervalList.append(x*interval)

filtersmp = [filters[intervalList[0]:intervalList[1]],
             filters[intervalList[1]:intervalList[2]],
             filters[intervalList[2]:intervalList[3]],
             filters[intervalList[3]:intervalList[4]],
             filters[intervalList[4]:intervalList[5]],
             filters[intervalList[5]:intervalList[6]],
             filters[intervalList[6]:intervalList[7]],
             filters[intervalList[7]:intervalList[8]],
             filters[intervalList[8]:intervalList[9]],
             filters[intervalList[9]:]]

interval = int(sys.argv[1])

filters = filtersmp[interval]

print('starting interval ', interval, ': ' , time.time()-start)

start = time.time()
data1 = pd.DataFrame(columns=['weekend', 'time_of_day', 'origin', 
                              'destination', 'count', 'price'])
total = len(filters)

baseindex = filters[0][0]

for [index, query, day, time_, origin, destination] in filters:
    filtered = data.query(query)
    count = len(filtered)
    if count>0:
        price = filtered['price'].mean()
    else:
        price = 0
    result = [day, time_, origin, destination, count, price]
    data1 = data1.append(pd.DataFrame([result], 
                              columns=['weekend', 'time_of_day', 'origin', 
                                       'destination', 'count', 'price']),
                              ignore_index = True)
    if index%100 == 0: 
        print('interval ', interval, ': ',round(time.time()-start, 2),': ', index-baseindex, '/', total,
              round(index/total*100-100*interval, 3),'%')

filename = 'parsed{}.csv'.format(interval)
data1.to_csv(filename)

print('written interval ', interval, ' to ', filename)