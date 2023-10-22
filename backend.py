import requests
import streamlit as st
API_KEY = "8e41178896564cda8f6141549232210"

def get_data(place=None, forecast_days=1, kind="Temperature"):
    if not place:
        return None
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={place}&days={forecast_days}"

    response = requests.get(url)
    content = response.json()
    date = []

    if "forecast" in content:
        content_filtered = content["forecast"]

        if kind == "Temperature":
            max_temp_list = []
            forecast_days_data = content_filtered["forecastday"]

            for day_data in forecast_days_data:
                date.append(day_data["date"])
                max_temp = day_data["day"]["maxtemp_c"]
                max_temp_list.append(max_temp)

            return date, max_temp_list

        elif kind == "Wind":
            wind_speed_list = []
            forecast_days_data = content_filtered["forecastday"]

            for day_data in forecast_days_data:
                date.append(day_data["date"])
                wind_speed = day_data["day"]["maxwind_kph"]
                wind_speed_list.append(wind_speed)

            return date, wind_speed_list
        elif kind == "Sky":
            sky_icon = []
            forecast_days_data = content_filtered["forecastday"]

            for day_data in forecast_days_data:
                date.append(day_data["date"])
                sky_condition = day_data["day"]["condition"]["icon"]
                sky_icon.append(f"https:{sky_condition}")
                print(sky_icon)
            return date, sky_icon
    return None




if __name__=="__main__":
    print(get_data(place="Tokyo", forecast_days=1, kind="Sky"))