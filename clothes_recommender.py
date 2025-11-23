# clothes_recommender.py

def temperature_recommendation(temp):
    """Returns clothing recommendation based on temperature."""
    if temp >= 30:
        # Changed print = (...) to return (...)
        return "It's very hot! Wear light cotton clothes, shorts, and a T-shirt."
    elif 20 <= temp < 30:
        # Changed print = (...) to return (...)
        return "The weather is warm. A light shirt or dress is suitable."
    elif 10 <= temp < 20:
        # Changed print = (...) to return (...)
        return "It’s cool. Wear a hoodie or a light jacket."
    elif 0 <= temp < 10:
        # Changed print = (...) to return (...)
        return "It's cold. Wear a heavy jacket, gloves, and warm pants."
    else:
        # Changed print = (...) to return (...)
        return "Extreme cold! Wear thermals, a thick coat, gloves, and a cap."

def weather_recommendation(condition):
    """Returns clothing recommendation based on weather condition."""
    condition = condition.lower()
    if condition == "sunny":
        # Changed print = (...) to return (...)
        return "Don't forget sunglasses and sunscreen."
    elif condition == "cloudy":
        # Changed print = (...) to return (...)
        return "Mild weather. You may carry a light jacket."
    elif condition == "rainy":
        # Changed print = (...) to return (...)
        return "Carry an umbrella or a raincoat. Wear waterproof shoes."
    elif condition == "windy":
        # Changed print = (...) to return (...)
        return "Wear a windcheater or windproof jacket."
    else:
        # Changed print = (...) to return (...)
        return "Weather condition not recognized. Dress comfortably!"