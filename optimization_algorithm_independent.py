import numpy as np
from itertools import accumulate

crops = ['Crop A', 'Crop B', 'Crop C']
cost_per_m2 = [10, 15, 20]
revenue_per_m2 = [20, 25, 30]
total_budget = 1000
total_area = 500

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