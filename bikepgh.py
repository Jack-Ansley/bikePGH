import argparse
import json
import requests
import math
import pandas as pd


class ArgStorage:
    def __init__(self, baseurl, command, x, y, stationid):
        self.baseurl = baseurl
        self.command = command
        self.x = x if x is not None else None
        self.y = y if y is not None else None
        self.stationid = stationid if stationid is not None else None


class StationInfo:
    def __init__(self, distance_from_origin, station_id, address):
        self.distance_from_origin = distance_from_origin
        self.station_id = station_id
        self.address = address


# 1
def total_bikes_func(instruct):
    station_status_url = instruct.baseurl + 'station_status.json'
    response = requests.get(station_status_url)
    response_obj = response.json()
    data_dict = response_obj.get('data')
    station_list = list(data_dict.get('stations'))
    count = 0
    for i in station_list:
        count = count + i.get('num_bikes_available')

    print('Parameters: None')
    print('Output: ', count)
    return


# 2
def total_docks_func(instruct):
    station_status_url = instruct.baseurl + 'station_status.json'
    response = requests.get(station_status_url)
    response_obj = response.json()
    data_dict = response_obj.get('data')
    station_list = list(data_dict.get('stations'))
    count = 0
    for i in station_list:
        count = count + i.get('num_docks_available')

    print('Parameters: None')
    print('Output: ', count)
    return


# 3
def percent_avail_func(instruct):
    station_status_url = instruct.baseurl + 'station_status.json'
    response = requests.get(station_status_url)
    response_obj = response.json()
    data_dict = response_obj.get('data')
    station_list = list(data_dict.get('stations'))
    value = 0
    for i in station_list:
        if instruct.stationid == i.get('station_id'):
            docks = i.get('num_docks_available')
            bikes = i.get('num_bikes_available')
    value = (docks / (bikes + docks))
    value = value * 100
    print('Parameters: ', instruct.stationid)
    print('Output: %', "{:.0f}".format(value))
    return


# 4
def closest_stations_func(instruct):
    station_status_url = instruct.baseurl + 'station_information.json'
    response = requests.get(station_status_url)
    response_obj = response.json()
    data_dict = response_obj.get('data')
    station_list = list(data_dict.get('stations'))
    x1 = float(instruct.x)
    y1 = float(instruct.y)
    dummy_first = StationInfo(9999999999, None, None)
    dummy_second = StationInfo(9999999999, None, None)
    dummy_third = StationInfo(9999999999, None, None)
    ranking = [dummy_first, dummy_second, dummy_third]
    for i in station_list:
        x2 = float(i.get('lon'))
        y2 = float(i.get('lat'))

        dist = math.sqrt((pow((x2 - x1), 2)) + (pow((y2 - y1), 2)))

        if ranking[0].distance_from_origin > dist:
            ranking[2] = ranking[1]
            ranking[1] = ranking[0]
            ranking[0] = StationInfo(dist, i.get('station_id'), i.get('name'))
        elif ranking[1].distance_from_origin > dist > ranking[0].distance_from_origin:
            ranking[2] = ranking[1]
            ranking[1] = StationInfo(dist, i.get('station_id'), i.get('name'))
        elif ranking[2].distance_from_origin > dist > ranking[1].distance_from_origin:
            ranking[2] = StationInfo(dist, i.get('station_id'), i.get('name'))

    print('Parameters: %f %f' % (x1, y1))
    print('Output=')
    print('%s, %s' % (ranking[0].station_id, ranking[0].address))
    print('%s, %s' % (ranking[1].station_id, ranking[1].address))
    print('%s, %s' % (ranking[2].station_id, ranking[2].address))


# 5
def closest_bike_func(instruct):
    station_status_url = instruct.baseurl + 'station_information.json'
    response = requests.get(station_status_url)
    response_obj = response.json()
    data_dict = response_obj.get('data')
    station_list_info = list(data_dict.get('stations'))

    station_status_url = instruct.baseurl + 'station_status.json'
    response = requests.get(station_status_url)
    response_obj = response.json()
    data_dict = response_obj.get('data')
    station_list_status = list(data_dict.get('stations'))

    x1 = float(instruct.x)
    y1 = float(instruct.y)
    shortest_dist = 10000000  # arbitratliy large value

    for i in station_list_status:
        if i.get('num_docks_available') > 0:
            check_id = i.get('station_id')
            for j in station_list_info:
                if check_id == j.get('station_id'):
                    x2 = float(j.get('lon'))
                    y2 = float(j.get('lat'))

                    dist = math.sqrt((pow((x2 - x1), 2)) + (pow((y2 - y1), 2)))
                    if dist < shortest_dist:
                        shortest_dist = dist
                        current_shortest_station = StationInfo(shortest_dist, j.get('station_id'), j.get('name'))

    print('Parameters: %f %f' % (x1, y1))
    print('Output = %s, %s' % (current_shortest_station.station_id, current_shortest_station.address))


# 6
def station_bike_avail_func(instruct):
    station_status_url = instruct.baseurl + 'station_information.json'
    response = requests.get(station_status_url)
    response_obj = response.json()
    data_dict = response_obj.get('data')
    station_list_info = list(data_dict.get('stations'))

    station_status_url = instruct.baseurl + 'station_status.json'
    response = requests.get(station_status_url)
    response_obj = response.json()
    data_dict = response_obj.get('data')
    station_list_status = list(data_dict.get('stations'))

    x1 = float(instruct.x)
    y1 = float(instruct.y)

    for i in station_list_info:
        if i.get('lon') == y1 and i.get('lat') == x1:
            check_id = i.get('station_id')
            for j in station_list_status:
                if check_id == j.get('station_id'):
                    bike_count = j.get('num_bikes_available')

    print('Parameters: %f %f' % (x1, y1))
    print('Output = %s, %s' % (check_id, bike_count))


commandParse = argparse.ArgumentParser()
commandParse.add_argument("baseurl", help='Valid prefix URL')
commandParse.add_argument("command", help='specifies which of the 6 commands to run')
commandParse.add_argument("param1", nargs='?')
commandParse.add_argument("param2", nargs='?')

args = commandParse.parse_args()

if args.param1 is not None and args.param2 is None:
    inargs = ArgStorage(args.baseurl, args.command, None, None, args.param1)
elif args.param1 is not None and args.param2 is not None:
    inargs = ArgStorage(args.baseurl, args.command, args.param1, args.param2, None)
else:
    inargs = ArgStorage(args.baseurl, args.command, None, None, None)

if inargs.command == 'total_bikes':
    print("Command: total_bikes")
    total_bikes_func(inargs)
elif inargs.command == 'total_docks':
    print("Command: total_docks")
    total_docks_func(inargs)
elif inargs.command == 'percent_avail':
    percent_avail_func(inargs)
    print("Command: percent_avail")
elif inargs.command == 'closest_stations':
    print("Command: closest_stations")
    closest_stations_func(inargs)
elif inargs.command == 'closest_bike':
    print("Command: closest_bike")
    closest_bike_func(inargs)
elif inargs.command == 'station_bike_avail':
    print("Command: station_bike_avail")
    station_bike_avail_func(inargs)
else:
    print("Invalid Argument! Exiting!\n")
