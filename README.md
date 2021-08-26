# bikePGH
Python program with 6 functions that will access a live feed of data from the bikePGH datastream.

### Command #1: Total bikes available
The command `total_bikes` will compute how many bikes are currently available over all stations in the entire HealthRidePGH network.

Sample invocation:
```
python3 bikepgh.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ total_bikes
```


### Command #2: Total docks available
The command `total_docks` will compute how many docks are currently available over all stations in the entire HealthRidePGH network.

Sample invocation:
```
python3 bikepgh.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ total_docks
```


### Command #3: Percentage of docks available in a specific station
The command `percent_avail` will compute how many docks are currently available for the specified station as a percentage over the total number of bikes and docks available. In this case, the station_id is given as a parameter.

Sample invocation:
```
python3 bikepgh.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ percent_avail 342885
```


### Command #4: Names of three closest HealthyRidePGH stations.
The command `closest_stations` will return the station_ids and the names of the three closest HealthyRidePGH stations based just on latitude and longtitude (of the stations and of the specified location). The first parameter is the latitude and the second parameter is the longtitude.

Sample invocation:
```
python3 bikepgh.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ closest_stations 40.444618 -79.954707
```


### Command #5: Name of the closest HealthyRidePGH station with available bikes
The command `closest_bike` will return the station_id and the name of the closest HealthyRidePGH station that has available bikes, given a specific latitude and longitude. The first parameter is the latitude and the second parameter is the longitude.

Sample invocation:
```
python3 bikepgh.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ closest_bike 40.444618 -79.954707
```


### Command #6: The number of bikes available at a bike station 
The command `station_bike_avail` will return the station_id and the number of bikes available at the station, given a specific latitude and longitude. The first parameter is the latitude and the second parameter is the longitude.

Sample invocation:
```
python3 bikepgh.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ station_bike_avail 40.444618 -79.954707
```
