from prometheus_client import start_http_server, Gauge
import requests, time

# Метрики
temperature = Gauge('weather_temperature_celsius', 'Temperature in Celsius')
windspeed = Gauge('weather_wind_speed', 'Wind speed in km/h')
winddirection = Gauge('weather_wind_direction', 'Wind direction in degrees')
cloudcover = Gauge('weather_cloud_cover', 'Cloud cover percentage')
apparent_temperature = Gauge('weather_apparent_temperature', 'Feels-like temperature')
pressure = Gauge('weather_pressure_hpa', 'Air pressure in hPa')
humidity = Gauge('weather_humidity_percent', 'Humidity percentage')
is_day = Gauge('weather_is_day', 'Is it day (1) or night (0)')
latitude = Gauge('weather_latitude', 'Latitude of the city')
longitude = Gauge('weather_longitude', 'Longitude of the city')
last_update = Gauge('weather_last_update_unix', 'Last update time in UNIX')

def collect_data():
    while True:
        try:
            url = (
                "https://api.open-meteo.com/v1/forecast?"
                "latitude=51.17&longitude=71.43&"
                "current=temperature_2m,relative_humidity_2m,apparent_temperature,"
                "pressure_msl,cloud_cover,wind_speed_10m,wind_direction_10m,is_day"
            )
            response = requests.get(url).json()
            data = response["current"]

            temperature.set(data["temperature_2m"])
            windspeed.set(data["wind_speed_10m"])
            winddirection.set(data["wind_direction_10m"])
            humidity.set(data["relative_humidity_2m"])
            pressure.set(data["pressure_msl"])
            cloudcover.set(data["cloud_cover"])
            apparent_temperature.set(data["apparent_temperature"])
            is_day.set(data["is_day"])
            last_update.set(time.time())
            latitude.set(51.17)
            longitude.set(71.43)

            print("Metrics updated successfully!")
        except Exception as e:
            print("Error:", e)
        time.sleep(20)

if __name__ == "__main__":
    start_http_server(8000)
    print("Custom Exporter started on port 8000")
    collect_data()
