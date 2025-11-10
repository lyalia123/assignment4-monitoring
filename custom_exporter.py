from prometheus_client import start_http_server, Gauge
import requests, time

# 🏙️ Метрики теперь с меткой 'city'
temperature = Gauge('weather_temperature_celsius', 'Temperature in Celsius', ['city'])
windspeed = Gauge('weather_wind_speed', 'Wind speed in km/h', ['city'])
winddirection = Gauge('weather_wind_direction', 'Wind direction in degrees', ['city'])
cloudcover = Gauge('weather_cloud_cover', 'Cloud cover percentage', ['city'])
apparent_temperature = Gauge('weather_apparent_temperature', 'Feels-like temperature', ['city'])
pressure = Gauge('weather_pressure_hpa', 'Air pressure in hPa', ['city'])
humidity = Gauge('weather_humidity_percent', 'Humidity percentage', ['city'])
is_day = Gauge('weather_is_day', 'Is it day (1) or night (0)', ['city'])
last_update = Gauge('weather_last_update_unix', 'Last update time in UNIX', ['city'])
latitude = Gauge('weather_latitude', 'Latitude of the city', ['city'])
longitude = Gauge('weather_longitude', 'Longitude of the city', ['city'])

def collect_data():
    # 🗺️ Список городов и их координат
    cities = {
        "Astana": (51.17, 71.43),
        "Almaty": (43.24, 76.88),
        "Shymkent": (42.31, 69.59)
    }

    while True:
        for city, (lat, lon) in cities.items():
            try:
                url = (
                    f"https://api.open-meteo.com/v1/forecast?"
                    f"latitude={lat}&longitude={lon}&"
                    "current=temperature_2m,relative_humidity_2m,apparent_temperature,"
                    "pressure_msl,cloud_cover,wind_speed_10m,wind_direction_10m,is_day"
                )
                response = requests.get(url, timeout=10).json()
                data = response["current"]

                # Устанавливаем значения с меткой города
                temperature.labels(city=city).set(data["temperature_2m"])
                windspeed.labels(city=city).set(data["wind_speed_10m"])
                winddirection.labels(city=city).set(data["wind_direction_10m"])
                humidity.labels(city=city).set(data["relative_humidity_2m"])
                pressure.labels(city=city).set(data["pressure_msl"])
                cloudcover.labels(city=city).set(data["cloud_cover"])
                apparent_temperature.labels(city=city).set(data["apparent_temperature"])
                is_day.labels(city=city).set(data["is_day"])
                last_update.labels(city=city).set(time.time())
                latitude.labels(city=city).set(lat)
                longitude.labels(city=city).set(lon)

                print(f"✅ Metrics updated for {city}")
            except Exception as e:
                print(f"⚠️ Error fetching data for {city}: {e}")
        time.sleep(60)

if __name__ == "__main__":
    start_http_server(8000)
    print("🌍 Custom Exporter started on port 8000")
    collect_data()
