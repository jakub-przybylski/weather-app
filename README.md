# weather-app

**A clean and fast weather application providing data about the weather in cities around the world. It was created by a student for developing own programming skills.**

## Installation

### Requirements:

* Python 3.10 or higher
* An API key from [OpenWeatherMap](https://openweathermap.org/api)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/jakub-przybylski/weather-app.git](https://github.com/jakub-przybylski/weather-app.git)
   cd weather-app
   ```
2. **Install dependencies:**
   ```bash
   pip install customtkinter requests pillow python-dotenv
   ```
3. **Configure your API Key:**
   ```bash
   Create a `.env` file in the root directory and add your OpenWeatherMap API key:
   env
   OPENWEATHER_API_KEY=your_api_key_here
   ```

## Usage & Features

### How to Use
1. Launch the application by running `python src/main.py`.
2. Type the desired city name into the input field at the top.
3. Click the **Search** button (or press Enter) to fetch the current weather.

### Key Features
* **Real-time Weather Data:** Retrieves live temperature, "feels like" temperature, general description, and wind speed via the OpenWeatherMap API.
* **Dynamic Weather Icons:** Automatically updates UI icons based on OpenWeatherMap condition IDs (e.g., sun, rain, snow, clouds, thunderstorm).
* **Modern GUI:** Built with `CustomTkinter` using a dark-mode theme and custom styling.
* **Error Handling:** Built-in safeguards for invalid city names, missing API keys, or missing graphic assets.

## Author 

* Name: Jakub Przybylski
* Email: jakubprzybylski676@gmail.com



