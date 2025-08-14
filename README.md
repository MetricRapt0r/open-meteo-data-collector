# Weather Data Collector

A Python script that fetches hourly weather data from public APIs (Open-Meteo) and saves it to CSV for analysis and visualization.

---

## Features
- Retrieve hourly temperature data for any city worldwide
- Automatically converts city name to coordinates using Geopy
- Saves data in CSV format and keeps historical records
- Easily extensible to include more weather parameters or visualization

---

## Requirements
- Python 3.9+
- Libraries:
  - `requests`
  - `pandas`
  - `geopy`

---

## Installation
Clone the repository:
```bash
git clone https://github.com/MetricRapt0r/open-meteo-data-collector.git
cd open-meteo-data-collector
```

---

## Install dependencies:
`pip install -r requirements.txt`

---

## Usage
Run the script:
`python weather_collector.py`
- Enter a city name when prompted.
- The script will fetch weather data for that city and save it to data/weather_data.csv.

---

## Example CSV output
```
latitude,longitude,datetime,temperature_C
45.4384,10.9916,2025-08-14 00:00,24.5
45.4384,10.9916,2025-08-14 01:00,23.8
```

---

## Future Improvements
- Add plots of temperature over time using matplotlib
- Save data to a database (e.g., PostgreSQL) for larger analysis
- Include more weather parameters (humidity, wind, precipitation)
- Telegram Bot

---

## License
MIT License

Copyright (c) 2025 Augustin Golovco

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

