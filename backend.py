import requests
API_KEY = "8e41178896564cda8f6141549232210"

def get_data(place, forecast_days=None, kind=None):
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

            return max_temp_list, date

        elif kind == "Wind":
            wind_speed_list = []
            forecast_days_data = content_filtered["forecastday"]

            for day_data in forecast_days_data:
                date.append(day_data["date"])
                wind_speed = day_data["day"]["maxwind_kph"]
                wind_speed_list.append(wind_speed)

            return wind_speed_list, date
    return None


if __name__=="__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))