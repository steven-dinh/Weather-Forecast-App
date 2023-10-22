import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather Forecast for the Next Days")
default_place = "Tokyo"
place = st.text_input("Place: ", default_place)

days = st.slider("Forecast Days", min_value=1, max_value=14,
                 help="Select the number of days to be displayed")
option = st.selectbox("Select data to view",
                      ("Temperature", "Wind", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

print(get_data(place, days, option))

if place:
    if option == "Temperature" or option == "Wind":
        d, t = get_data(place, days, option)
        unit = "C" if option == "Temperature" else "KPH"

        figure = px.line(x=d, y=t, labels={"x": "Date", "y": f"{option} ({unit})"})
        st.plotly_chart(figure)

    elif option == "Sky":
        date, sky_icons = get_data(place, days, option)
        cols = st.columns(len(sky_icons))
        for i in range(len(sky_icons)):
            cols[i].image(sky_icons[i], caption=date[i],width=115)