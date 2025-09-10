import requests

def weather(city="Delhi"):
    API_Key = "1de0209d1de781abdd67f521ffa631c8"  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        
        return {
            "description": description,
            "temp": temp,
            "humidity": humidity
        }
