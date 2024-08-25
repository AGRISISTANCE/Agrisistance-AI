import os
from fastapi import FastAPI, HTTPException
import requests
import numpy as np
import joblib
import pandas as pd
from chatbot.chat_service import ChatRequest  # Import the ChatRequest model

# Load the model and scaler
model = joblib.load('crop_model_simplified.joblib')
scaler = joblib.load('crop_scaler.joblib')

# Initialize FastAPI app
app = FastAPI()

# Input and parameters
total_budget = 1000  # Placeholder, will come from request
total_area = 500     # Placeholder, will come from request

@app.post("/predict")
async def predict_crops(input_data: dict):
    try:
        # Extract inputs from request
        input_ph = input_data["ph"]
        input_temperature = input_data["temperature"]
        input_rainfall = input_data["rainfall"]
        input_humidity = input_data["humidity"]
        input_nitrogen = input_data["nitrogen"]
        input_phosphorus = input_data["phosphorus"]
        input_potassium = input_data["potassium"]
        input_o2 = input_data["o2"]
        total_budget = input_data["budget"]
        total_area = input_data["area"]
        
        new_data = np.array([[input_ph, input_temperature, input_rainfall, input_humidity, 
                              input_nitrogen, input_phosphorus, input_potassium, input_o2]])
        
        top_10_predictions = predict_top_10_crops(model, scaler, new_data)
        
        # Financial data processing
        df = pd.read_csv('crop_finance.csv')
        filtered_df = df[df['Crop'].isin(top_10_predictions)]
        cost_per_m2 = filtered_df['cost_per_area'].tolist()
        weight_area = filtered_df['weight_area'].tolist()
        amount_area = filtered_df['amount_area'].tolist()
        revenue_per_m2 = [w * a for w, a in zip(weight_area, amount_area)]

        # Genetic algorithm for optimal crop allocation
        best_solution = run_genetic_algorithm(cost_per_m2, revenue_per_m2, total_budget, total_area, top_10_predictions)
        
        # Create a response dictionary
        response = {
            "crops": {crop: best_solution[i] - (best_solution[i-1] if i > 0 else 0) for i, crop in enumerate(top_10_predictions)},
            "total_cost": sum([best_solution[i] * cost_per_m2[i] for i in range(len(top_10_predictions))]),
            "total_revenue": sum([best_solution[i] * revenue_per_m2[i] for i in range(len(top_10_predictions))]),
            "total_profit": sum([best_solution[i] * revenue_per_m2[i] for i in range(len(top_10_predictions))]) - sum([best_solution[i] * cost_per_m2[i] for i in range(len(top_10_predictions))])
        }

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Your existing functions, adapted as necessary:

def predict_top_10_crops(model, scaler, new_data):
    new_data_scaled = scaler.transform(new_data)
    probabilities = model.predict_proba(new_data_scaled)[0]
    top_10_crops = [model.classes_[i] for i in np.argsort(probabilities)[::-1][:10]]
    return top_10_crops

def fitness_function(individual, cost_per_m2, revenue_per_m2, crops, total_budget, total_area):
    total_cost = 0
    total_revenue = 0
    total_area_used = 0
    
    for i, crop in enumerate(crops):
        area_for_crop = individual[i]
        total_cost += area_for_crop * cost_per_m2[i]
        total_revenue += area_for_crop * revenue_per_m2[i]
        total_area_used += area_for_crop
    
    if total_cost > total_budget or total_area_used > total_area:
        return 0
    else:
        return total_revenue - total_cost

def initialize_population(population_size, crops, total_area):
    population = []
    for _ in range(population_size):
        individual = np.random.randint(0, total_area + 1, size=len(crops))
        individual.sort()
        population.append(individual)
    return population

def select_parents(population, fitness_function, cost_per_m2, revenue_per_m2, crops, total_budget, total_area):
    population_array = np.array(population)
    fitness_scores = [fitness_function(individual, cost_per_m2, revenue_per_m2, crops, total_budget, total_area) for individual in population]
    total_fitness = sum(fitness_scores)
    if total_fitness == 0:
        return population_array[np.random.choice(len(population), size=2)]
    probabilities = [score / total_fitness for score in fitness_scores]
    parents = population_array[np.random.choice(len(population), size=2, p=probabilities)]
    return parents

def crossover(parent1, parent2, crops, total_area):
    child = []
    for i in range(len(crops)):
        if i == 0:
            child.append(np.random.randint(0, min(parent1[i], parent2[i]) + 1))
        else:
            min_val = min(parent1[i], parent2[i])
            max_val = max(parent1[i], parent2[i])
            child.append(np.random.randint(min_val, max_val + 1))
    child.sort()
    return child

def mutate(individual, mutation_rate, crops, total_area):
    mutated_individual = individual.copy()
    for i in range(len(crops)):
        if np.random.rand() < mutation_rate:
            if i == 0:
                mutated_individual[i] = np.random.randint(0, mutated_individual[i] + 1)
            else:
                min_val = 0 if i == 0 else mutated_individual[i-1]
                max_val = total_area if i == len(crops) - 1 else mutated_individual[i+1]
                mutated_individual[i] = np.random.randint(min_val, max_val + 1)
    mutated_individual.sort()
    return mutated_individual

def run_genetic_algorithm(cost_per_m2, revenue_per_m2, total_budget, total_area, crops):
    population_size = 100
    num_generations = 100
    mutation_rate = 0.1
    population = initialize_population(population_size, crops, total_area)
    for _ in range(num_generations):
        new_population = []
        for _ in range(population_size // 2):
            parents = select_parents(population, fitness_function, cost_per_m2, revenue_per_m2, crops, total_budget, total_area)
            child1 = crossover(parents[0], parents[1], crops, total_area)
            child2 = crossover(parents[0], parents[1], crops, total_area)
            new_population.append(mutate(child1, mutation_rate, crops, total_area))
            new_population.append(mutate(child2, mutation_rate, crops, total_area))
        population = new_population
    
    best_individual = max(population, key=lambda x: fitness_function(x, cost_per_m2, revenue_per_m2, crops, total_budget, total_area))
    return best_individual

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        headers = {
            'Content-Type': 'application/json',
            'api_token': os.getenv('API_TOKEN')
        }
        payload = request.dict()
        response = requests.post(
            'https://api.afro.fit/api_v2/api_wrapper/chat/completions',
            json=payload,
            headers=headers
        )
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# To run the server, use the command:
# uvicorn main:app --reload
