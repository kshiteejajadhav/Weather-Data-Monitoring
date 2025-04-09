# IoT Weather Data Monitoring with OpenWeatherMap & ThingSpeak

## Overview
This project demonstrates a complete end-to-end IoT pipeline for **real-time environmental data monitoring**. Using **live data** fetched from the OpenWeatherMap API, the system pushes real-time telemetry (temperature, humidity, pressure, wind speed) to **ThingSpeak**, where it is visualized and analyzed through built-in charts and MATLAB tools.

The solution simulates a typical smart weather station dashboard using only Python, public weather APIs, and cloud-hosted IoT platforms.

---

## Features

- Fetches **live weather data** using OpenWeatherMap API
- Publishes data to **ThingSpeak IoT channel** using HTTP
- Supports key environmental parameters:
  - Temperature
  - Humidity
  - Pressure
  - Wind Speed
- Runs periodically with customizable time intervals (In this case 10 min)
- Includes **MATLAB-based advanced visualization widgets**
- Real-time data plotted on ThingSpeak dashboard

---

## Tools & Technologies Used

- **Python 3.7+**
- [OpenWeatherMap API](https://openweathermap.org/api)
- [ThingSpeak IoT Cloud](https://thingspeak.com/)
- `requests` Python library

---

## Project Structure

```bash
      weather-data-iot/
      ├── weatherdata.py         # Python script to fetch and upload weather data
      ├── README.md              # Project documentation (this file)
      ├── requirements.txt       # Required Python dependencies
      ├── visualizations/        # Screenshots of dashboard visualizations
      │   ├── fields.png
      │   └── advanced_views.png

```

Setup & Configuration
  
1. Prerequisites
  	•	Python 3.7 or above installed
  	•	requests installed via:    

```pip install -r requirements.txt```

2. API Configuration
	•	Get your OpenWeatherMap API Key
	•	Create a ThingSpeak Channel with 4 fields:
	•	Field 1: Temperature
	•	Field 2: Humidity
	•	Field 3: Pressure
	•	Field 4: Wind Speed
	•	Locate the Write API Key and Channel ID from ThingSpeak

3. Script Customization

Update weatherdata.py with:
	•	Your OpenWeatherMap API key
	•	Your ThingSpeak channel ID and write key
	•	Your city name or latitude/longitude if needed

⸻

Running the Script

```python3 weatherdata.py```

This will:
	•	Fetch data from OpenWeatherMap
	•	Push it to your ThingSpeak channel
	•	Repeat after every interval (default: 10 minutes)

⸻

Visualization

Data will automatically appear in the ThingSpeak channel’s visual charts. You can also:
	•	Add line plots, gauges, or numeric displays
	•	Use MATLAB tools for:
	•	Temperature histograms
	•	Compass plots (for wind direction if available)
	•	Scatter plots (temperature vs. humidity)
	•	Time series overlay

Examples:
	•	Basic Field Charts: Temperature, Humidity, Pressure, Wind Speed
	•	Advanced MATLAB Views: Correlations, Trends, Distribution

⸻

Reflection

Building this project provided hands-on experience in integrating live public data sources with cloud-based IoT platforms. It offered insight into how real-world weather monitoring systems operate — from fetching and parsing API data, to securing API keys, and deploying structured data pipelines. The visual feedback on ThingSpeak allowed me to validate my logic and better understand time-series trends in environmental data.

⸻

Requirements

```requests```

Install using:

```pip install requests```



⸻

Notes
	•	Do not share your API keys publicly.
	•	This project uses real data, no simulation was involved.

⸻
