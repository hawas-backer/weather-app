import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for The next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days",min_value=1,max_value=5,
                 help="Select the number of days for forecast")
option = st.selectbox("Select data to view",("Temperature","sky"))
st.header(f"{option} for the next {days} in {place}")

if place:
    try:
        filtered_data = get_data(place,days,option)

        if option =="Temperature":
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates,y=temperatures,labels={"x":"Dates","y":"Temperature (c)"})
            st.plotly_chart(figure)
        if option =="sky":
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [sky.lower()+".png" for sky in sky_condition]
            st.image(image_paths,width=115 )
    except KeyError:
        st.write("The city is not found")
