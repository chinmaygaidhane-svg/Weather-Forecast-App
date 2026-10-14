import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file.Checks any environment variable in the .env file and loads it into the environment   

API_KEY = os.getenv("WEATHER_API_KEY")  # Get the API key from environment variable
st.set_page_config(page_title='Weather Forecast App',page_icon="https://img.freepik.com/premium-photo/sun-moon-emoji-set-white-background_41969-14626.jpg")

st.title("weather forecast ")
st.write("Enter the city Name and click the button to fetch the weather data")
city = st.text_input("Enter city name")
if (st.button("Get Weather Data")):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
    if(response.status_code == 200):
        st.success("Weather data fetched successfully")
        data =response.json() # .json() extract the json and convert it into a python dictionary

        
    
        #Extract weatther data from the response
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_condition = data['weather'][0]['description']
        city_name = data['name']
        country_name = data['sys']['country']

        st.subheader(f"{city_name},{country_name}")



        
        #Create Four Columns
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        col1.metric('temperature 🌡️',f"{temperature}°C")
        col2.metric('humidity 💧',f"{humidity}%")
        col3.metric('Wind speed 🌬️',f"{wind_speed} m/s")
        col4.metric('Weather Condition 🌤️',f"{weather_condition}")
else:
    st.error("Invalid city name ")
