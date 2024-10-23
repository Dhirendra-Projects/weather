import requests

#Input for city and  country
country_code = input("Enter the counrty:")
city_name = input("Enter the city name :")

api_key ="3014bf2397a00bf15e1601a9a99521dc"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}&units=metric"

# Request the data from the API
responce = requests.get(url)
if responce.status_code == 200:
    data =responce.json()

    # Extracting weather information
    humidity = data["main"]["humidity"]
    temperature = int(data["main"]["temp"])
    pressure = data["main"]["pressure"]

    # Dispaly the weather info
    print(f"\nWeather is {city_name.upper()},{country_code.upper()}")
    print("Description:",data["weather"][0]["description"])
    print(f"Temperature: {temperature}°C ")  # Degree Celsius
    print(f"Humidity: {humidity}%")
    print(f"Presssure: {pressure} hPa") # hPa= Hecto Pascal
else:
    print("City not found!!!")   
