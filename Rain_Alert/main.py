import requests

api_key = "0baf5fe5a5e3f046fbae7b3a14622f99"

parameters = {
    "lat":-0.498007,
    "lon":36.328430,
    "appid":api_key,
    "exclude":"main,wind,sys,base,visibility,clouds"

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()
weather_today = data["weather"][0]["id"]
print(weather_today)

if weather_today <700:
    print("will rain")