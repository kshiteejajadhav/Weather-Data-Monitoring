import requests
import time
# === OpenWeatherMap API Configuration ===
API_KEY = "c6f84c808e5682431ec56bfc28724df5"
LAT = "43.0481"   # Syracuse latitude
LON = "-76.1474"  # Syracuse longitude
WEATHER_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
# === ThingSpeak Configuration ===
THINGSPEAK_URL = "https://api.thingspeak.com/update"
WRITE_API_KEY = "57NIMQ5KPMVNERYH"
CHANNEL_FIELDS = {
    "field1": "temperature",
    "field2": "humidity",
    "field3": "pressure",
    "field4": "wind_speed"
}
def fetch_weather_data():
    try:
        response = requests.get(WEATHER_URL)
        response.raise_for_status()
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        return {
            "temperature": temp,
            "humidity": humidity,
            "pressure": pressure,
            "wind_speed": wind_speed
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
def send_to_thingspeak(data):
    payload = {
        "api_key": WRITE_API_KEY,
        "field1": data["temperature"],
        "field2": data["humidity"],
        "field3": data["pressure"],
        "field4": data["wind_speed"]
    }
    try:
        response = requests.post(THINGSPEAK_URL, data=payload)
        if response.status_code == 200 and response.text != "0":
            print(f"Data sent to ThingSpeak successfully! Entry ID: {response.text}")
        else:
            print("Failed to send data to ThingSpeak.")
    except Exception as e:
        print(f"Error sending data to ThingSpeak: {e}")
def main():
    while True:
        weather = fetch_weather_data()
        if weather:
            print(f"Weather: {weather}")
            send_to_thingspeak(weather)
        else:
            print("Skipping ThingSpeak update due to error.")

        time.sleep(600)#10 minutes
if __name__ == "__main__":
    main()