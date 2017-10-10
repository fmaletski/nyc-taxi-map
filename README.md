# NYC Taxi & Limousine Commission Trip Data - Interactive Choropleth
by Fernando Maletski

## Summary
This interactive data visualization illustrates when and where the NYC yellow taxis pick up and drop off passengers in the city. The data was obtained from the New York City Taxi & Limousine Commission.

## Design

### ETL (Extract, Transform, Load)
The data was downloaded from the NYC TLC website (http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml). Due to the size of the dataset, I chose to use just the latest yellow taxi file, June 2017 (https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2017-06.csv), but the modules and the visualization html created are able to handle any data from this source with minimal to no modification.

Also, because of the size of the original dataset, I am unable to upload it to github, but it can be easily downloaded using the provided link above.

During prototyping, the location id translation dataset (https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv, renamed locid.csv) was used.

The last dataset used is the shapefile (https://s3.amazonaws.com/nyc-tlc/misc/taxi_zones.zip), it was converted to GeoJSON using Gipong's shp2geojson.js (https://github.com/gipong/shp2geojson.js). The original file (taxi_zones.zip) and the resulting (zones.geojson) are included in this repository.

Transforming the dataset to its final form is done in a simple 3 step process. This design decision was made due to the large amount of time needed to complete each step, and compartmentalization of possible bugs.

#### Initial parsing 
Using the module parser.py, each trip is reduced to common attributes, eg. from JFK Airport to Lower East Side, during mornings on weekdays. The resulting trips are counted, and the average price is computed for each combination of attributes.

To speed up the process, parser.py is created in a way that the total amount of combinations is divided into 10 unique lists, so they can be run in parallel without multiprocessing complications, simply using as many terminal windows as a computer can handle. In my case (intel i7-5820k), I ran all 10 processes at the same time, and this stop took about 9 hours to complete.

Here's the list of commands necessary to complete this stage:

```
$ python3 parser.py yellow_tripdata_2017-06.csv 0
$ python3 parser.py yellow_tripdata_2017-06.csv 1
$ python3 parser.py yellow_tripdata_2017-06.csv 2
$ python3 parser.py yellow_tripdata_2017-06.csv 3
$ python3 parser.py yellow_tripdata_2017-06.csv 4
$ python3 parser.py yellow_tripdata_2017-06.csv 5
$ python3 parser.py yellow_tripdata_2017-06.csv 6
$ python3 parser.py yellow_tripdata_2017-06.csv 7
$ python3 parser.py yellow_tripdata_2017-06.csv 8
$ python3 parser.py yellow_tripdata_2017-06.csv 9
```
These commands will create 10 files into the ./data folder: parsed(0-9).csv to be used in the next stage.

#### Merging
The module merger.py uses the 10 previously created files, parsed(0-9).csv, to create a json file (finalData.json) containing all the information necessary to produce the visualization. 

By design, as this visualization uses a fairly large final dataset file, 4 MB+, I chose to include all the arithmetic operations in this part of the project, to reduce drawing times, and smooth the animations.

```
$ python3 merger.py
```

#### Final Dataset

This final stage merges the original zones.json and finalData.json into one single file to be used by the visualization (data.geojson).

I chose to do this because it's simple to use each path element to contain all the data necessary to draw it, no matter what filters are used, not just the format of the zone. This way, it's simple to change the color based on user selection, and show information using tooltips.

```
$ python3 finalDataWriter.py
```

This final command concludes the ETL part of this project.

### Map Design

#### Shapefile to GeoJSON

One surprising difficult step was converting the original NYC TLC shapefile to a format readable by D3.JS. The main problem was not converting the format per se, but the coordinate system.

I first created python module using pyshp to handle the task, it was simple enough, but when I used the resulting file to draw the map, it was nowhere to be found! No amount of translation or D3.JS commands allowed me to find it.

I tried using online tools, like http://mapshaper.org/, to no avail and more advanced programs like QGIS (qgis.org) when I discovered that the problem was that the coordinate reference system used by the shapefile was different than the one used by GeoJSON (https://tools.ietf.org/html/rfc7946#section-4).

Surprisingly, one simple JS script created by Gipong called shp2geojson.js (https://github.com/gipong/shp2geojson.js) was the solution to my problems, thank you Gipong!

#### Interface layout

As this is an interactive visualization, it is important to create a pleasant UI for user, many times an ugly or overly complicated UI hampers otherwise great content.

To create an UI that is both beautiful and functional, I used Bootstrap (https://getbootstrap.com/docs/3.3/). By including all the necessary controls on the top of the page, the map becomes uncluttered and easier to understand.

<img src="./img/first-layout.png" alt="Drawing" style="width: 700px;"/>

At this phase, no data was used to color the zones, and no button was working. It's just the basic layout. It can be visualized by accessing the [map-layout.html](./proto/map-layout.html) file.
