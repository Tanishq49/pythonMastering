import requests

# Your API key and city
api_key = "9cfdec8f3b12427aa90161004253007"
city = input("Enter the name of your city:")

# API endpoint
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

# Make request
response = requests.get(url)

# Handle response
if response.status_code == 200:
    data = response.json()
    location = data['location']['name']
    temp_c = data['current']['temp_c']
    condition = data['current']['condition']['text']
    humidity = data['current']['humidity']
    wind_kph = data['current']['wind_kph']
    
    print(f"📍 Location: {location}")
    print(f"🌡️ Temperature: {temp_c}°C")
    print(f"🌤️ Condition: {condition}")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌬️ Wind: {wind_kph} kph")
else:
    print("❌ Failed to fetch weather data:", response.status_code)

