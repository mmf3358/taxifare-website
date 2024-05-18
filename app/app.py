import streamlit as st
import requests


'''
# TaxiFareModel front
'''
if 'pickup_datetime' not in st.session_state:
    st.session_state.pickup_datetime = 0

if 'pickup_longitude' not in st.session_state:
    st.session_state.pickup_longitude = 0
    
if 'pickup_latitude' not in st.session_state:
    st.session_state.pickup_latitude = 0
    
if 'dropoff_longitude' not in st.session_state:
    st.session_state.dropoff_longitude = 0

if 'passenger_count' not in st.session_state:
    st.session_state.passenger_count = 0

date = st.date_input('Data', value = None)
time = st.time_input("Hora",  value = None)

pickup_datetime = f'{date} {time}'
pickup_longitude = st.text_input('Pickup Longitude')
pickup_latitude = st.text_input('Pickup Latidude')
dropoff_longitude = st.text_input('Dropoff Longitude')
dropoff_latitude = st.text_input('Dropoff Latitude')
passenger_count = st.text_input('Passenger Count')
    
params = {
        'pickup_datetime': pickup_datetime, 
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
        }

url = 'https://taxifare.lewagon.ai/predict'

res = requests.get(url, params).json()

while 'fare' not in res:
    st.stop()

res['fare']


#https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20
# &pickup_longitude=40.7614327
# &pickup_latitude=-73.9798156
# &dropoff_longitude=40.6513111
# &dropoff_latitude=-73.8803331
# &passenger_count=2