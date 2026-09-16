import requests 
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENWEATHER_API_KEY")

def error():
    messagebox.showerror("Failed to save changes. Please try again.")

def get_data(city_name):

    if not key or not city_name.strip():
        return None

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}&units=metric&lang=pl"

    try:
        response = requests.get(url)
        if response.status_code() == 200:
            data = response.json()
            return {
                "city": data["name"],
                "temp": f"{round(data['main']['temp'])}°C",
                "feels_like": f"Perceived: {round(data['main']['feels_like'])}°C",
                "description": data["weather"][0]["description"].capitalize(),
                "wind": f"Wind: {round(data['wind']['speed'] * 3.6)} km/h"
            }
        else:
            return None
    except:
        error()
        return None