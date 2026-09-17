import requests 
import os
from tkinter import messagebox
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENWEATHER_API_KEY")
#function for error communicate 
def error():
    messagebox.showerror("Error", "Failed to fetch weather data. Please try again.")

# function for getting data from api
def get_data(city_name):

    if not key or not city_name.strip():
        return None

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}&units=metric&lang=en"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            # creating json file for holding the data
            data = response.json()
            return {
                "city": data["name"],
                "temp": f"{round(data['main']['temp'])}°C",
                "feels_like": f"Perceived: {round(data['main']['feels_like'])}°C",
                "description": data["weather"][0]["description"].capitalize(),
                "wind": f"Wind: {round(data['wind']['speed'] * 3.6)} km/h",
                "id": data["weather"][0]["id"]
            }
        else:
            error()
            return None
    except:
        error()
        return None

def get_image(weather_id):
    if 200 <= weather_id <= 232:
        return "assets/thunderstorm.png"
    elif 300 <= weather_id <= 321:
        return "assets/drizzle.png"
    elif 500 <= weather_id <= 531:
        return "assets/rain.png"
    elif 600 <= weather_id <= 622:
        return "assets/snow.png"
    elif 701 <= weather_id <= 781:
        return "assets/atmosphere.png"
    elif weather_id == 800:
        return "assets/clear.png"
    elif 801 <= weather_id <= 804:
        return "assets/clouds.png"
    else:
        return "assets/face.png"
        

