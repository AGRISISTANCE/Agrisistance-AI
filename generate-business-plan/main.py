# main.py

import os
import json
from typing import List, Dict
from dotenv import load_dotenv, find_dotenv
from services.business_plan_generator import generate_business_plan


load_dotenv(find_dotenv())

API_TOKEN = os.getenv('API_TOKEN')
API_URL = os.getenv('API_URL')

# Input data
crops_data = [
    {"name": "Wheat", "predicted_revenue": 10000, "weight": 5000, "area": 100},
    {"name": "Corn", "predicted_revenue": 15000, "weight": 7500, "area": 150}
]
soil_params = {"pH": 6.5, "nitrogen": 20, "phosphorus": 15, "potassium": 25}
weather_data = {"annual_rainfall": 1000, "average_temperature": 22}
budget = 50000
total_area = 300

def main():
    result = generate_business_plan(
        crops_data=crops_data,
        soil_params=soil_params,
        weather_data=weather_data,
        budget=budget,
        total_area=total_area,
        api_token=API_TOKEN,
        api_url=API_URL
    )
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
