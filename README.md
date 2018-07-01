# GeoFlask

**GeoFlask** is an alternative to the Google Geolocation API.

Current Version **0.1**

## Objective

The main goal is to create a cost effective alternative to the Google Geolocation API. The data that will be used come from the OpenStreetMap project. The raw data will then be processed by ElasticSearch, and then served by an API.

## Installation
    brew install protobuf
    export CC=/usr/local/Cellar/gcc/8.1.0/bin/g++-8
    pip install osmread

## Commands
    ./geoflaskenv/bin/python main.py

## OSM Source Files
* https://download.geofabrik.de/europe/switzerland.html

## Versions


#### 1.0
* Consume osm.pbf files.
* Format for elasticsearch.
* Test environment.

#### 2.0
* ElasticSearch parsing.
* Serve as an API.
* osm.pbf automation via S3.

#### 3.0
* API authentication.
* Cloudfront replication.

#### 4.0
* React frontend.
* Stripe.
