import requests

import psycopg2
import psycopg2.extras

from datetime import datetime

import logging

def fetch_data():

    api_token = '50518584f04612c7'

    url ='http://api.wunderground.com/api/'+api_token+'/geolookup/conditions/q/Maldives/Male.json'
    r = requests.get(url).json()
    data = r ['current_observation']
    location = data['observation_location']['full']
    weather = data['weather']
    wind_str =data['wind_string']
    temp = data['temp_f']
    humidity = data['relative_humidity']
    percip = data['precip_today_string']
    icon_url = data['icon_url']
    observation_time =data['observation_time']


    print(location,temp,weather)
#Dbopen

    try:

        conn = psycopg2.connect(dbname='daaet229tjvhkr',user='zbnyfewkdmcwqm',password ='e2c87a8c7d9fb24e62a1fd73630aed732436396c0e85a69ff5d978d19d6c2fa4',host ='ec2-107-21-109-15.compute-1.amazonaws.com',port ='5432')
        print('connections open')

    except:

        return
    else:

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("""INSERT INTO roseapp_reading(location, weather, wind_str, temp, humidity, percip, icon_url, observation_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",(location, weather, wind_str, temp, humidity, percip, icon_url, observation_time))

        conn.commit()
        cur.close()
        conn.close()

        print('done')

fetch_data()