import requests

API_KEY = "e813e5eca2711f07fbcb2479073114f1"
CITY = "New York"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    print(f"Weather in {CITY}: {data['weather'][0]['description']}, {data['main']['temp']}°C")
else:
    print("Error:", data)
