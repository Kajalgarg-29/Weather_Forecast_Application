import requests

city_name="Delhi"
API_key="a8ae76d6cf3e9e6de68155d483ab576f"


response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}")

if response.status_code==200:
    data=response.json()
    weather_main =data["main"]

    Temperature = int(weather_main['temp']-273.15)
    print(f"Temerature:{Temperature}°C")
else:
    print("INTERNET NOT WORKING")
