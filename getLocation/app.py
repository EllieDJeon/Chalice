import os, sys, boto3, ast, googlemaps, re
from chalice import Chalice, BadRequestError, NotFoundError
import numpy as np
import pandas as pd
gmaps = googlemaps.Client(key='AIzaSyCL8LykrYfie-rTNsi1KJOkF-n-V0yoct0')

app = Chalice(app_name='test70-chalice')
app.debug = True

def getAppAddress(param_json):
    # latlng = '0.0000,0.0000'
    # http https://jv17oiv64f.execute-api.us-west-2.amazonaws.com/api/getLocation params='{"lat":39.7166,"lng":116.5420}'
    # param_json = ast.literal_eval(app.current_request.json_body['params'])
    
    lat = param_json['lat']
    lng = param_json['lng']

    display_add = ''
    country = ''
    location = ''

    try:
        # lan, lng= latlng.split(',')
        location = gmaps.reverse_geocode((float(lat),float(lng)))
        lst=[]
        for add in location[0]['address_components']:
            lst.append(add['short_name'])
        address = ','.join(lst)
        
        country = re.findall('[A-Z][A-Z]', address)[-1]
        address = address.split(',')
        indices = [i for i, s in enumerate(address) if country in s]
        countyIdx = indices[-1] # idx for country code in the address list
        display_add = address[countyIdx-2]+', '+address[countyIdx-1]
    except: pass
        
    return display_add


# # Index information
@app.route('/')
def index():
    return {
        'status': 'API is available',
        'discription':'This api is for getting an address from given lat and long info',
        'user':'CarVi@ejeon'
        }


@app.route('/getLocation', methods=['POST'], content_types=['application/json'])
def getLocation():
    # latlng = '0.0000,0.0000'
    # http https://jv17oiv64f.execute-api.us-west-2.amazonaws.com/api/getLocation params='{"source": {"lat": 35.5786,"lng": 139.7447}, "destination": {"lat": 35.7378,"lng": 139.7604}}'    param_json = ast.literal_eval(app.current_request.json_body['params'])

    city_json = {}

    try:
        city_json['source'] = getAppAddress(param_json['source'])
        city_json['destination'] = getAppAddress(param_json['destination'])

    except: pass
    response = {'location':param_json, 'city':city_json}

    return response



@app.route('/location', methods=['POST'], content_types=['application/json'])
def getAddress():
    # latlng = '0.0000,0.0000'
    # http https://jv17oiv64f.execute-api.us-west-2.amazonaws.com/api/location params='{"latlng":"39.7166,116.5420"}'
    param_json = ast.literal_eval(app.current_request.json_body['params'])
    
    latlng = param_json['latlng']

    display_add = ''
    country = ''
    location = ''

    try:
        lat, lng= latlng.split(',')
        location = gmaps.reverse_geocode((float(lat),float(lng)))
        lst=[]
        for add in location[0]['address_components']:
            lst.append(add['short_name'])
        address = ','.join(lst)
        
        country = re.findall('[A-Z][A-Z]', address)[-1]
        address = address.split(',')
        indices = [i for i, s in enumerate(address) if country in s]
        countyIdx = indices[-1] # idx for country code in the address list
        display_add = address[countyIdx-2]+', '+address[countyIdx-1]
    except: pass
        
    return {'location':latlng, 'address' : display_add, 'country': country}

@app.route('/secretinfo')
def secretinfo():
    info = {
        'googlemaps key': 'AIzaSyCL8LykrYfie-rTNsi1KJOkF-n-V0yoct0'
        }
    return {'secretinfo' : info}



