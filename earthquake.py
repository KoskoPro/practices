import requests
import re

while True:
    start_time = input('Enter the start time (YYYY-MM-DD): ')
    if re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}$', start_time):
        break
    print('Please enter a valid start date format')

while True:
    end_time = input('Enter the end time (YYYY-MM-DD): ')
    if re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}$', end_time):
        break
    print('Please enter a valid end date format')

while True:
    latitude = input('Enter the latitude: ')
    if latitude.isdigit():
        if 180 >= int(latitude) >= (-180):
            break
        print('Enter latitude between -180 and 180')
    print('Enter latitude int type')

while True:
    longitude = input('Enter the longitude: ')
    if longitude.isdigit():
        if 90 >= int(longitude) >= (-90):
            break
        print('Enter longitude between -90 and 90')
    print('Enter longitude int type')

while True:
    max_radius = input('Enter the max_radius: ')
    if max_radius.isdigit():
        if 20001.6 >= int(max_radius) >= 0:
            break
        print('Enter max_radius between 0 and 20001.6')
    print('Enter max_radius int type')

while True:
    magnitude = input('Enter the min magnitude: ')
    if magnitude.isdigit():
        if 10 >= int(magnitude) >= 0:
            break
        print('Enter min magnitude between 0 and 10')
    print('Enter min magnitude int type')

# Test data
# start_time = '2022-01-01'
# end_time = '2022-01-02'
# latitude = '0'
# longitude = '0'
# max_radius = '20000'
# magnitude = '3'


url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers={'Accept': 'Aplication/json'}, params={
    'format': 'geojson',
    'starttime': start_time,
    'endtime': end_time,
    'latitude': latitude,
    'longitude': longitude,
    'maxradiuskm': max_radius,
    'minmagnitude': magnitude
})
data = response.json()

for i in range(len(data['features'])):
    print(
        f"{i + 1}. Place: {data['features'][i]['properties']['place']}. Magnitude: {data['features'][i]['properties']['mag']}")
