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



