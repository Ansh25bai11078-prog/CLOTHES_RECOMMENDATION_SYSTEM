# main.py
import clothes_recommender

print("----- Clothes Recommendation System -----")

# User inputs
temperature = float(input("Enter temperature (°C): "))
weather = input("Enter weather condition (sunny/cloudy/rainy/windy): ")

print("\n--- Recommendation ---")

# Using module functions
# These lines now correctly capture the strings returned by the functions
temp_msg = clothes_recommender.temperature_recommendation(temperature)
weather_msg = clothes_recommender.weather_recommendation(weather)

# Output
print(temp_msg)
print(weather_msg)
print("\nStay comfortable and have a great day!")