import numpy as np
import joblib
import logging
from itertools import accumulate
import io
#version scikit-learn==1.3.2

#inputs

input_ph = 6.5  
input_temperature = 25.0  
input_rainfall = 200.0  #api
input_humidity = 70.0  #api
input_nitrogen = 50.0  
input_phosphorus = 40.0  
input_potassium = 30.0  
input_o2 = 21.0  
total_budget = 1000 #from user($)
total_area = 500 #from user (m2)








result = []

# Set up logging so we can track what's happening
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the pre-trained model directly from the file
def load_model(model_file):
    logging.info("Loading the machine learning model...")
    model = joblib.load(model_file)
    return model

# Load the scaler
def load_scaler(scaler_file):
    logging.info("Loading the scaler...")
    return joblib.load(scaler_file)

# Predict the top 10 crops that match the input data
def predict_top_10_crops(model, scaler, new_data):
    logging.info("Making predictions for the top 10 most suitable crops...")
    new_data_scaled = scaler.transform(new_data)
    probabilities = model.predict_proba(new_data_scaled)[0]
    top_10_crops = [model.classes_[i] for i in np.argsort(probabilities)[::-1][:10]]
    return top_10_crops

# Function to predict the best crops based on input variables
def predict_interactive(model, scaler):
    logging.info("Using predefined input data to predict top 10 crops...")
    
    new_data = np.array([[input_ph, input_temperature, input_rainfall, input_humidity, 
                          input_nitrogen, input_phosphorus, input_potassium, input_o2]])
    
    top_10_predictions = predict_top_10_crops(model, scaler, new_data)
    
    print("\nTop 10 crop predictions:")
    for i, crop in enumerate(top_10_predictions, 1):
        print(f"{i}. {crop}")
    
    return top_10_predictions

# Load the model from the zipped file and the scaler from the regular file

model_file = 'crop_model_simplified.joblib'
scaler_file = 'crop_scaler.joblib'

model = load_model(model_file)
scaler = load_scaler(scaler_file)

# Run the prediction function and store the result in the 'result' variable
result = predict_interactive(model, scaler)




import pandas as pd


df = pd.read_csv('crop_finance.csv')

crops = result

filtered_df = df[df['Crop'].isin(crops)]

cost_per_m2 = filtered_df['cost_per_area'].tolist()
weight_area = filtered_df['weight_area'].tolist()
amount_area = filtered_df['amount_area'].tolist()

revenue_per_m2 = [w * a for w, a in zip(weight_area, amount_area)]






population_size = 100
num_generations = 100
mutation_rate = 0.1

def fitness_function(individual):
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

def initialize_population():
    population = []
    for _ in range(population_size):
        individual = np.random.randint(0, total_area + 1, size=len(crops))
        individual.sort()
        population.append(individual)
    return population

def select_parents(population):
    population_array = np.array(population)
    fitness_scores = [fitness_function(individual) for individual in population]
    total_fitness = sum(fitness_scores)
    if total_fitness == 0:
        return population_array[np.random.choice(len(population), size=2)]
    probabilities = [score / total_fitness for score in fitness_scores]
    parents = population_array[np.random.choice(len(population), size=2, p=probabilities)]
    return parents

def crossover(parent1, parent2):
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

def mutate(individual):
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

def run_genetic_algorithm():
    population = initialize_population()
    for _ in range(num_generations):
        new_population = []
        for _ in range(population_size // 2):
            parents = select_parents(population)
            child1 = crossover(parents[0], parents[1])
            child2 = crossover(parents[0], parents[1])
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
        population = new_population
    
    best_individual = max(population, key=fitness_function)
    return best_individual


best_solution = run_genetic_algorithm()


print("Optimal allocation:")
for i, crop in enumerate(crops):
    print(f"{crop}: {best_solution[i] - (best_solution[i-1] if i > 0 else 0)} m²")
print(f"Total cost: {sum([best_solution[i] * cost_per_m2[i] for i in range(len(crops))])}")
print(f"Total revenue: {sum([best_solution[i] * revenue_per_m2[i] for i in range(len(crops))])}")
print(f"Total profit: {sum([best_solution[i] * revenue_per_m2[i] for i in range(len(crops))]) - sum([best_solution[i] * cost_per_m2[i] for i in range(len(crops))])}")