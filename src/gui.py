import customtkinter as ctk

def run_app():

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    
    root = ctk.CTk()
    root.grid_columnconfigure(0, weight=1)
    root.title("Weather App")
    root.geometry("300x300")

    label_text = ctk.CTkLabel(root, text="Today is...", font=("Roboto", 16,"bold"))
    label_text.grid(row=0, column=0, padx=20, pady=5)

    root.mainloop()