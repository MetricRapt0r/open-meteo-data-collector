import requests
import pandas as pd
from datetime import datetime
from geopy.geocoders import Nominatim # Import geopy for geolocation
import os

# Output folder and file configuration
OUTPUT_DIR = "data"  # Directory to store CSV files
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "weather_data.csv")  # CSV file path


def fetch_weather_data(LAT, LON):
    """
    Fetch weather data from Open-Meteo API.
    Returns:
        dict: JSON response from the API.
    """
    print("[INFO] Fetching weather data...")

    # Open-Meteo API URL for hourly temperature data
    API_URL = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&hourly=temperature_2m"
    
    # Make a GET request to the API
    response = requests.get(API_URL, timeout=10)
    
    response.raise_for_status()
    
    # Convert the API response from JSON into a Python dictionary
    data = response.json()
    
    print("[INFO] Data received successfully")
    return data

def process_weather_data(data):
    """
    Extract and format the data into a Pandas DataFrame.
    Args:
        data (dict): Raw JSON data from the API.
    Returns:
        pd.DataFrame: DataFrame with latitude, longitude, datetime, and temperature columns.
    """
    # Get the hourly section of the JSON, or an empty dict if not present
    hourly = data.get("hourly", {})
    
    # Create a DataFrame with latitude, longitude, datetime, and temperature columns
    df = pd.DataFrame({
        "latitude": [LAT] * len(hourly.get("time", [])),    # Repeat latitude for each time entry
        "longitude": [LON] * len(hourly.get("time", [])),   # Repeat longitude for each time entry
        "datetime": pd.to_datetime(hourly.get("time", [])),  # Convert ISO strings to datetime objects
        "temperature_C": hourly.get("temperature_2m", [])    # Get temperature data
    })
    
    return df

def save_to_csv(df):
    """
    Save the data in CSV format.
    Args:
        df (pd.DataFrame): DataFrame containing weather data.
    """
    # Ensure the output directory exists; create if it doesn't
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    if os.path.exists(OUTPUT_FILE):
        # If CSV already exists, append new data without headers to maintain history
        df.to_csv(OUTPUT_FILE, mode="a", header=False, index=False)
    else:
        # If CSV doesn't exist, create it with headers
        df.to_csv(OUTPUT_FILE, index=False)
    
    print(f"[INFO] Data saved to {OUTPUT_FILE}")


def get_coordinates_for_city(city_name: str):
    # Return (latitude, longitude) for a given city using geopy
    geolocator = Nominatim(user_agent="weather_data_collector")
    location = geolocator.geocode(city_name)
    if location is None:
        return None, None
    return location.latitude, location.longitude

if __name__ == "__main__":
    try:
        city = input("Enter city name: ")
        LAT, LON = get_coordinates_for_city(city)

        while LAT is None or LON is None:
            print(f"[ERROR] Could not find coordinates for {city}. Please try again.")
            city = input("Enter city name: ")
            LAT, LON = get_coordinates_for_city(city)

        print(f"[INFO] Coordinates for {city}: {LAT}, {LON}")

        raw_data = fetch_weather_data(LAT, LON)
        df_weather = process_weather_data(raw_data)
        save_to_csv(df_weather)

        print("[SUCCESS] Script completed.")

    except Exception as e:
        print(f"[ERROR] {e}")
