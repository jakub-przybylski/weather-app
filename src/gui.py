import customtkinter as ctk

def run_app():

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    
    root = ctk.CTk()
    root.grid_columnconfigure(0, weight=1)
    root.title("Weather App")
    root.geometry("300x300")

    # Space to enter the name of ther city
    label_input = ctk.CTkEntry(root, placeholder_text="Enter the city", font=("Robot", 16, "bold"))
    label_input.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

    # Button to search the city
    label_button = ctk.CTkButton(root, text="Search", font=("Roboto", 16, "bold"))
    label_button.grid(row=0, column=1, padx=10, pady=5)

    # text with the name of the city
    label_name = ctk.CTkLabel(root, text="city", font=("Roboto", 16,"bold"))
    label_name.grid(row=1, column=0, columnspan=2, padx=20, pady=5)

    # temperature in the city
    label_temperature = ctk.CTkLabel(root, text="20", font=("Roboto", 16,"bold"))
    label_temperature.grid(row=2, column=0, columnspan=2, padx=20, pady=5)

    # description of the weather in the city
    label_description = ctk.CTkLabel(root, text="description", font=("Roboto", 16,"bold"))
    label_description.grid(row=3, column=0, columnspan=2, padx=20, pady=5)

    label_perceivedTemperature = ctk.CTkLabel(root, text="20", font=("Roboto", 10))
    label_perceivedTemperature.grid(row=4, column=0, padx=20, pady=5)

    label_wind = ctk.CTkLabel(root, text="20", font=("Roboto", 10))
    label_wind.grid(row=4, column=1, padx=20, pady=5)

    root.mainloop()