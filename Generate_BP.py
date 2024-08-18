import requests
import json
import os
from typing import List, Dict

# Set your API token as an environment variable for security
os.environ['OPENAI_API_TOKEN'] = 'your_api_token_here'

# API endpoint
API_URL = 'https://api.afro.fit/api_v2/api_wrapper/chat/completions'

def get_available_models():
    """Fetch available models from the API."""
    headers = {'accept': 'application/json'}
    response = requests.get('https://api.afro.fit/api_v2/api_wrapper/models', headers=headers)
    return response.json()

def generate_business_plan(crops_data: List[Dict], soil_params: Dict, weather_data: Dict, budget: float):
    """
    Generate a business plan using the OpenAI API.
    
    :param crops_data: List of dictionaries containing crop info (name, predicted revenue, weight, area)
    :param soil_params: Dictionary of soil parameters
    :param weather_data: Dictionary of weather data
    :param budget: Total budget for the project
    :return: Generated business plan text
    """
    # Construct the prompt for the API
    prompt = f"""Generate a detailed agricultural business plan with the following sections:

1. Resources:
   - Recommend the number of workers needed and how many can be afforded based on the budget of ${budget}.
   - Suggest machines to invest in for the crops: {', '.join([crop['name'] for crop in crops_data])}.
   - Recommend pesticides, soil vitamins, and products based on these soil parameters: {soil_params}.
   - Suggest potential improvements for the farm.

2. Crops:
   - For each crop ({', '.join([crop['name'] for crop in crops_data])}), provide:
     - Best practices for soil preparation and crop maintenance.
     - Growth maintenance tips.
     - Recommended area and budget allocation (use the provided data).

3. Weather:
   Based on this weather data: {weather_data}, suggest:
   - Best measures to ensure high revenue.
   - Protective measures for the crops.

4. Soil/Crops Maintenance:
   - Provide a detailed maintenance schedule, including:
     - Watering frequency and amount.
     - Fertilization schedule.
     - Pest control measures.

5. Profits:
   - Provide expected numbers and total investment returns based on the crop data: {crops_data}.
   - Suggest procedures to improve profitability.

6. Other Recommendations:
   - Any additional suggestions to improve growth, land use, or investment returns.

Please provide a comprehensive and detailed plan for each section."""

    # Prepare the API request
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {os.environ['OPENAI_API_TOKEN']}"
    }
    
    data = {
        'model': 'gpt-3.5-turbo',  # You can change this to a different model if needed
        'messages': [{'role': 'user', 'content': prompt}],
        'temperature': 0.7,
        'max_tokens': 2000  # Adjust this based on the desired length of the response
    }

    # Make the API call
    response = requests.post(API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Example usage
if __name__ == "__main__":
    # Sample data - replace with your actual data
    crops_data = [
        {"name": "Wheat", "predicted_revenue": 10000, "weight": 5000, "area": 100},
        {"name": "Corn", "predicted_revenue": 15000, "weight": 7500, "area": 150}
    ]
    soil_params = {"pH": 6.5, "nitrogen": 20, "phosphorus": 15, "potassium": 25}
    weather_data = {"annual_rainfall": 1000, "average_temperature": 22}
    budget = 50000

    # Get available models
    models = get_available_models()
    print("Available models:", models)

    # Generate the business plan
    business_plan = generate_business_plan(crops_data, soil_params, weather_data, budget)
    print("\nGenerated Business Plan:")
    print(business_plan)