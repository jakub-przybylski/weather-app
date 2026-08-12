import customtkinter as ctk

def run_app():

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    
    root = ctk.CTk()
    root.title("Weather App")
    root.geometry("300x300")

    label_text = ctk.CtkLabel(root, text="", font=("Roboto", 16,"bold") )

    root.mainloop()