import pandas as pd
import pymongo
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image

# Setting up page configuration
icon = Image.open("D:/Airnbn/airbnb.png")
st.set_page_config(page_title= "AirBNB Analysis",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# To analyze Airbnb data using MongoDB Atlas """})
st.markdown("<h1 style='text-align: center; color: white;'>AirBNB Analysis</h1>", unsafe_allow_html=True)

def set_background():
    st.markdown(f""" 
                    <style>.stApp {{
                            background: url("https://wallpaperset.com/w/full/4/6/c/380280.jpg");
                            background-size: cover}}
                    </style>
                """
                ,unsafe_allow_html=True) 
    
set_background()

# Top Menu
selected = option_menu(None, ["Home","Overview","Explore"], 
                       icons=["house","search","heart"],
                       default_index=0,
                       orientation="horizontal",
                       styles={"nav-link": {"font-size": "27px", "text-align": "centre", "margin": "0px", "--hover-color": "#FF5A5F"},
                               "icon": {"font-size": "27px"},
                               "container" : {"max-width": "6000px"},
                               "nav-link-selected": {"background-color": "#ff0000"}})

# CREATING CONNECTION WITH MONGODB ATLAS AND RETRIEVING THE DATA
client = pymongo.MongoClient(
    f"mongodb+srv://jamuvishnu108:@cluster0.Jamuna01pqwt2iu.mongodb.net/?retryWrites=true&w=majority")
mydb=['sample_airbnb']
mycollection=mydb['listingsAndReviews']