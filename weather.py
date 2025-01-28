import streamlit as st
import pandas as pd
import requests
import json

st.set_page_config(layout='wide')

title_text = '''<h1 style='font-size : 55px;text-align:center;color:purple;background-color:lightgrey;'>WEATHER APP</h1>'''
st.markdown(title_text,unsafe_allow_html=True)

df = pd.read_csv(r"C:\Users\ASUS\Documents\GUVI ZEN CLASSES\MAINT BOOT\Horse Race Prediction\cities_r2.csv")

city_list = df['name_of_city'].tolist()

col1,col2 = st.columns(2)

with col1:

    title_text = '''<h1 style='font-size: 32px;text-align: center;color:#00ff80;'>Select the City to know its weather</h1>'''
    st.markdown(title_text, unsafe_allow_html=True)

    option = st.selectbox("Select the City:",city_list,index=None,placeholder="Select the City")


    if st.button('Submit'):

        api_key = '803ab481b9228021a9ef1c937112099a'
        lang = 'en'

        api_url = f'https://api.openweathermap.org/data/2.5/weather?q={option}&appid={api_key}&units=metric&lang={lang}'
        w_data = requests.get(api_url)
        data = w_data.json()
        #print(data)
        try:
            weather_data = {'City':data.get('name'),'Weather':data['weather'][0]['main'],'Description':data['weather'][0]['description'],
                        "Temperature in Celcius":data['main']['temp'],'Min_temp':data['main']['temp_min'],'Max_temp':data['main']['temp_max'],
                        'Pressure':data['main']['pressure'],'Humidity':data['main']['humidity']}
            #print(weather_data)
            keys_list = list(weather_data.keys())
            weather_df = pd.DataFrame(weather_data,index=range(0,1))
            st.dataframe(weather_df)
            if weather_data['Weather'] == 'Clouds' or weather_data['Weather'] == 'Haze':
                st.subheader(":red[Please] :orange[Take] :rainbow[Umbrella]")
            else:
                st.subheader(':red[Please] :rainbow[Take Cap]')
        except:
            st.write('Kindly try other city')

with col2:
    st.write("  ")
    st.write("  ")
    st.image('weather_image_3.jpg')