import logging
from model.load_model import load_model, load_scaler
from utils.load_helpers import load_crop_financial_data
from utils.predictions import predict_interactive
from utils.display_results import display_optimal_allocation
from optimization_algorithm.genetic_algorithm import run_genetic_algorithm

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Input Specifications
input_ph = 8.5  
input_temperature = 20.0  
input_rainfall = 700.0  
input_humidity = 70.0  
input_nitrogen = 400.0  
input_phosphorus = 400.0  
input_potassium = 300.0  
input_o2 = 21.0  
total_budget = 1000  # User-defined budget ($)
total_area = 500  # User-defined total area (m²)

# Genetic Algorithm parameters(do not modify)
population_size = 200
num_generations = 800
mutation_rate = 0.2
crossover_rate = 0.8

# Load the model and scaler
model_file = 'model/crop_model_simplified.joblib'
scaler_file = 'model/crop_scaler.joblib'
model = load_model(model_file)
scaler = load_scaler(scaler_file)

# Predict top 10 crops based on input data
crops = predict_interactive(model, scaler, input_ph, input_temperature, input_rainfall, 
                            input_humidity, input_nitrogen, input_phosphorus, input_potassium, input_o2)

# Load crop financial data
crop_finance_file = 'data/crop_finance.csv'
cost_per_m2, weight_area, revenue_per_m2 = load_crop_financial_data(crop_finance_file, crops)

# Run the genetic algorithm to optimize crop allocation
best_solution = run_genetic_algorithm(crops, cost_per_m2, revenue_per_m2, total_area, total_budget, 
                                      population_size, num_generations, mutation_rate, crossover_rate)

# Display the optimal allocation and expected returns
display_optimal_allocation(crops, best_solution, cost_per_m2, weight_area, revenue_per_m2, total_area, total_budget)
