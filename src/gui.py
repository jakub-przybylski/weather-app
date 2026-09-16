import customtkinter as ctk
from PIL import Image
from logic import get_data

def run_app():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    root = ctk.CTk()
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.title("Weather App")
    root.geometry("400x440")

    # space to enter the name of ther city
    label_input = ctk.CTkEntry(root, placeholder_text="Enter the city", font=("Segoe UI", 20, "bold"))
    label_input.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    # text with the name of the city
    label_name = ctk.CTkLabel(root, text=" ", font=("Segoe UI", 40,"bold"))
    label_name.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    # temperature in the city
    label_temperature = ctk.CTkLabel(root, text=" ", font=("Segoe UI", 40,"bold"))
    label_temperature.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    # description of the weather in the city
    label_description = ctk.CTkLabel(root, text=" ", font=("Segoe UI", 32,"bold"))
    label_description.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    # image 
    description_image = ctk.CTkImage(light_image=Image.open("assets/face.png"), dark_image=Image.open("assets/face.png"), size=(140, 70))

    label_image = ctk.CTkLabel(root, text="", image=description_image)
    label_image.grid(row=5, column=0, columnspan=2, padx=10, pady=3, sticky="ew")

    # perceived temperature
    label_perceivedTemperature = ctk.CTkLabel(root, text=" ", font=("Segoe UI", 20))
    label_perceivedTemperature.grid(row=6, column=0, padx=10, pady=5, sticky="ew")

    # wind
    label_wind = ctk.CTkLabel(root, text=" ", font=("Segoe UI", 20))
    label_wind.grid(row=6, column=1, padx=10, pady=5, sticky="ew")

    def search():
        name = label_input.get()
        weather = get_data(name)

        label_name.configure(text=f"{name}")
        label_temperature.configure(text=weather["temp"])
        label_description.configure(text=weather["description"])
        label_perceivedTemperature.configure(text=weather["feels_like"])
        label_wind.configure(text=weather["wind"])

    # button to search the city
    label_button = ctk.CTkButton(root, text="Search", font=("Segoe UI", 20, "bold"), command=search)
    label_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    root.mainloop()