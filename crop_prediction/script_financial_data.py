


import csv

# Specify the path to your CSV file
csv_file_path = 'primary.csv'

# Specify the column name you want to print
column_name = 'Crop'

# Open the CSV file
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)

    # Print the contents of the specified column
    for row in csv_reader:
        print(row[column_name])

data={
'lemon': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 2.0},
'lentil': {'minO2': 18, 'maxO2': 21, '$/kg': 1.0, 'kg/m²': 0.6},
'lettuce': {'minO2': 18, 'maxO2': 21, '$/kg': 2.5, 'kg/m²': 3.0},
'lime': {'minO2': 18, 'maxO2': 21, '$/kg': 1.2, 'kg/m²': 1.5},
'loquat': {'minO2': 18, 'maxO2': 21, '$/kg': 4.0, 'kg/m²': 2.5},
'longan': {'minO2': 18, 'maxO2': 21, '$/kg': 6.0, 'kg/m²': 2.5},
'lychee': {'minO2': 18, 'maxO2': 21, '$/kg': 5.0, 'kg/m²': 2.0},
'mango': {'minO2': 18, 'maxO2': 21, '$/kg': 2.5, 'kg/m²': 2.5},
'mandarin': {'minO2': 18, 'maxO2': 21, '$/kg': 2.0, 'kg/m²': 2.0},
'mulberry': {'minO2': 18, 'maxO2': 21, '$/kg': 4.0, 'kg/m²': 3.0},
'mung bean': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 1.0},
'mushroom': {'minO2': 18, 'maxO2': 21, '$/kg': 5.0, 'kg/m²': 2.5},
'mustard': {'minO2': 18, 'maxO2': 21, '$/kg': 1.0, 'kg/m²': 1.2},
'nectarine': {'minO2': 18, 'maxO2': 21, '$/kg': 3.0, 'kg/m²': 2.0},
'okra': {'minO2': 18, 'maxO2': 21, '$/kg': 2.0, 'kg/m²': 1.5},
'olive': {'minO2': 18, 'maxO2': 21, '$/kg': 2.0, 'kg/m²': 0.5},
'onion': {'minO2': 18, 'maxO2': 21, '$/kg': 1.0, 'kg/m²': 4.0},
'orange': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 2.5},
'oregano': {'minO2': 18, 'maxO2': 21, '$/kg': 8.0, 'kg/m²': 0.5},
'papaya': {'minO2': 18, 'maxO2': 21, '$/kg': 1.2, 'kg/m²': 4.0},
'parsnip': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 3.0},
'passion fruit': {'minO2': 18, 'maxO2': 21, '$/kg': 3.5, 'kg/m²': 2.5},
'pea': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 1.2},
'peach': {'minO2': 18, 'maxO2': 21, '$/kg': 2.5, 'kg/m²': 2.0},
'pear': {'minO2': 18, 'maxO2': 21, '$/kg': 2.0, 'kg/m²': 2.5},
'peppermint': {'minO2': 18, 'maxO2': 21, '$/kg': 15.0, 'kg/m²': 0.3},
'persimmon': {'minO2': 18, 'maxO2': 21, '$/kg': 3.0, 'kg/m²': 2.0},
'pineapple': {'minO2': 18, 'maxO2': 21, '$/kg': 1.0, 'kg/m²': 5.0},
'plum': {'minO2': 18, 'maxO2': 21, '$/kg': 2.5, 'kg/m²': 2.5},
'pomegranate': {'minO2': 18, 'maxO2': 21, '$/kg': 3.0, 'kg/m²': 3.0},
'potato': {'minO2': 18, 'maxO2': 21, '$/kg': 0.3, 'kg/m²': 4.5},
'prickly pear': {'minO2': 18, 'maxO2': 21, '$/kg': 2.0, 'kg/m²': 2.0},
'pumpkin': {'minO2': 18, 'maxO2': 21, '$/kg': 1.0, 'kg/m²': 5.0},
'hemp': {'minO2': 18, 'maxO2': 21, '$/kg': 1.0, 'kg/m²': 0.5},
'honeydew': {'minO2': 18, 'maxO2': 21, '$/kg': 1.0, 'kg/m²': 3.5},
'jackfruit': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 2.5},
'jabuticaba': {'minO2': 18, 'maxO2': 21, '$/kg': 6.0, 'kg/m²': 2.0},
'kale': {'minO2': 18, 'maxO2': 21, '$/kg': 3.0, 'kg/m²': 2.5},
'kiwi': {'minO2': 18, 'maxO2': 21, '$/kg': 2.0, 'kg/m²': 2.5},
'kohlrabi': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 3.5},
'kumquat': {'minO2': 18, 'maxO2': 21, '$/kg': 4.0, 'kg/m²': 2.0},
'lavender': {'minO2': 18, 'maxO2': 21, '$/kg': 40.0, 'kg/m²': 0.2},
'apricot': {'minO2': 18, 'maxO2': 21, '$/kg': 3.5, 'kg/m²': 2.0},
'artichoke': {'minO2': 18, 'maxO2': 21, '$/kg': 2.5, 'kg/m²': 1.5},
'asparagus': {'minO2': 18, 'maxO2': 21, '$/kg': 4.0, 'kg/m²': 0.5},
'avocado': {'minO2': 18, 'maxO2': 21, '$/kg': 3.0, 'kg/m²': 1.2},
'banana': {'minO2': 18, 'maxO2': 21, '$/kg': 0.5, 'kg/m²': 10.0},
'barley': {'minO2': 18, 'maxO2': 21, '$/kg': 0.3, 'kg/m²': 0.7},
'basil': {'minO2': 18, 'maxO2': 21, '$/kg': 10.0, 'kg/m²': 1.5},
'bean': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 1.0},
'beetroot': {'minO2': 18, 'maxO2': 21, '$/kg': 1.2, 'kg/m²': 3.5},
'bell pepper': {'minO2': 18, 'maxO2': 21, '$/kg': 2.5, 'kg/m²': 4.0},
'black gram': {'minO2': 18, 'maxO2': 21, '$/kg': 1.2, 'kg/m²': 0.8},
'blackberry': {'minO2': 18, 'maxO2': 21, '$/kg': 6.0, 'kg/m²': 2.5},
'blueberry': {'minO2': 18, 'maxO2': 21, '$/kg': 7.5, 'kg/m²': 1.0},
'broccoli': {'minO2': 18, 'maxO2': 21, '$/kg': 2.0, 'kg/m²': 2.5},
'buckwheat': {'minO2': 18, 'maxO2': 21, '$/kg': 1.0, 'kg/m²': 0.6},
'cabbage': {'minO2': 18, 'maxO2': 21, '$/kg': 0.5, 'kg/m²': 4.5},
'carrot': {'minO2': 18, 'maxO2': 21, '$/kg': 1.0, 'kg/m²': 3.0},
'cantaloupe': {'minO2': 18, 'maxO2': 21, '$/kg': 1.2, 'kg/m²': 3.0},
'cauliflower': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 3.0},
'celery': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 2.0},
'chickpea': {'minO2': 18, 'maxO2': 21, '$/kg': 1.0, 'kg/m²': 0.7},
'chili pepper': {'minO2': 18, 'maxO2': 21, '$/kg': 3.5, 'kg/m²': 1.2},
'clementine': {'minO2': 18, 'maxO2': 21, '$/kg': 2.5, 'kg/m²': 1.8},
'coconut': {'minO2': 18, 'maxO2': 21, '$/kg': 0.4, 'kg/m²': 0.5},
'corn': {'minO2': 18, 'maxO2': 21, '$/kg': 0.3, 'kg/m²': 2.5},
'cranberry': {'minO2': 18, 'maxO2': 21, '$/kg': 5.0, 'kg/m²': 1.5},
'cucumber': {'minO2': 18, 'maxO2': 21, '$/kg': 1.2, 'kg/m²': 6.0},
'custard apple': {'minO2': 18, 'maxO2': 21, '$/kg': 4.0, 'kg/m²': 2.0},
'date': {'minO2': 18, 'maxO2': 21, '$/kg': 3.0, 'kg/m²': 2.0},
'dragon fruit': {'minO2': 18, 'maxO2': 21, '$/kg': 5.0, 'kg/m²': 3.0},
'durian': {'minO2': 18, 'maxO2': 21, '$/kg': 15.0, 'kg/m²': 1.0},
'elderberry': {'minO2': 18, 'maxO2': 21, '$/kg': 5.0, 'kg/m²': 1.5},
'fennel': {'minO2': 18, 'maxO2': 21, '$/kg': 4.0, 'kg/m²': 2.0},
'fig': {'minO2': 18, 'maxO2': 21, '$/kg': 3.0, 'kg/m²': 2.0},
'flax': {'minO2': 18, 'maxO2': 21, '$/kg': 2.0, 'kg/m²': 0.4},
'garlic': {'minO2': 18, 'maxO2': 21, '$/kg': 2.5, 'kg/m²': 2.0},
'ginger': {'minO2': 18, 'maxO2': 21, '$/kg': 3.0, 'kg/m²': 1.5},
'grape': {'minO2': 18, 'maxO2': 21, '$/kg': 2.0, 'kg/m²': 3.5},
'grapefruit': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 3.0},
'green bean': {'minO2': 18, 'maxO2': 21, '$/kg': 1.8, 'kg/m²': 2.5},
'guava': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 4.0},
'turnip': {'minO2': 18, 'maxO2': 21, '$/kg': 1.2, 'kg/m²': 4.0},
'vanilla': {'minO2': 18, 'maxO2': 21, '$/kg': 500, 'kg/m²': 0.02},
'walnut': {'minO2': 18, 'maxO2': 21, '$/kg': 7.0, 'kg/m²': 0.6},
'watermelon': {'minO2': 18, 'maxO2': 21, '$/kg': 0.3, 'kg/m²': 3.5},
'wheat': {'minO2': 18, 'maxO2': 21, '$/kg': 0.2, 'kg/m²': 0.7},
'yam': {'minO2': 18, 'maxO2': 21, '$/kg': 1.0, 'kg/m²': 3.0},
'zucchini': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 3.5},
'alfalfa': {'minO2': 18, 'maxO2': 21, '$/kg': 0.25, 'kg/m²': 2.0},
'almond': {'minO2': 18, 'maxO2': 21, '$/kg': 5.5, 'kg/m²': 0.8},
'amaranth': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 1.0},
'apple': {'minO2': 18, 'maxO2': 21, '$/kg': 2.0, 'kg/m²': 2.5},
'quince': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 2.5},
'radish': {'minO2': 18, 'maxO2': 21, '$/kg': 1.5, 'kg/m²': 4.5},
'raspberry': {'minO2': 18, 'maxO2': 21, '$/kg': 6.0, 'kg/m²': 2.0},
'red clover': {'minO2': 18, 'maxO2': 21, '$/kg': 0.6, 'kg/m²': 1.5},
'rye': {'minO2': 18, 'maxO2': 21, '$/kg': 0.3, 'kg/m²': 0.5},
'salad green': {'minO2': 18, 'maxO2': 21, '$/kg': 4.0, 'kg/m²': 2.5},
'sorghum': {'minO2': 18, 'maxO2': 21, '$/kg': 0.2, 'kg/m²': 1.2},
'spearmint': {'minO2': 18, 'maxO2': 21, '$/kg': 2.0, 'kg/m²': 1.0},
'spinach': {'minO2': 18, 'maxO2': 21, '$/kg': 3.0, 'kg/m²': 3.0},
'starfruit': {'minO2': 18, 'maxO2': 21, '$/kg': 7.0, 'kg/m²': 3.0},
'strawberry': {'minO2': 18, 'maxO2': 21, '$/kg': 4.5, 'kg/m²': 2.5},
'sunflower': {'minO2': 18, 'maxO2': 21, '$/kg': 0.7, 'kg/m²': 0.8},
'sweet potato': {'minO2': 18, 'maxO2': 21, '$/kg': 1.0, 'kg/m²': 4.0},
'tangerine': {'minO2': 18, 'maxO2': 21, '$/kg': 2.5, 'kg/m²': 1.5},
'tobacco': {'minO2': 18, 'maxO2': 21, '$/kg': 0.1, 'kg/m²': 2.0},
'tomato': {'minO2': 18, 'maxO2': 21, '$/kg': 2.5, 'kg/m²': 5.0}}

import pandas as pd


# Load primary.csv
primary_df = pd.read_csv('primary.csv')

# Add minO2 and maxO2 to the dataset
primary_df['minO2'] = primary_df['Crop'].map(lambda x: data.get(x, {}).get('minO2'))
primary_df['maxO2'] = primary_df['Crop'].map(lambda x: data.get(x, {}).get('maxO2'))

# Save updated primary.csv
primary_df.to_csv('primary_updated.csv', index=False)

# Create crop_finance.csv
def calculate_finance(crop_name):
    crop_info = data.get(crop_name, {})
    kg_per_m2 = crop_info.get('kg/m²', 0)
    price_per_kg = crop_info.get('$/kg', 0)
    weight_area = kg_per_m2
    amount_area = weight_area * price_per_kg
    return weight_area, amount_area

# Prepare data for crop_finance.csv
crop_finance_data = []
for crop in data:
    weight_area, amount_area = calculate_finance(crop)
    crop_finance_data.append({'Crop': crop, 'weight_area': weight_area, 'amount_area': amount_area})

# Create DataFrame and save to crop_finance.csv
crop_finance_df = pd.DataFrame(crop_finance_data)
crop_finance_df.to_csv('crop_finance.csv', index=False)


data2={
       'quince': {'cost_per_m²': 3.75},
    'radish': {'cost_per_m²': 1.0},
    'raspberry': {'cost_per_m²': 12.0},
    'red clover': {'cost_per_m²': 0.9},
    'rye': {'cost_per_m²': 0.15},
    'salad green': {'cost_per_m²': 10.0},
    'sorghum': {'cost_per_m²': 0.24},
    'spearmint': {'cost_per_m²': 2.0},
    'spinach': {'cost_per_m²': 9.0},
    'starfruit': {'cost_per_m²': 21.0},
    'strawberry': {'cost_per_m²': 11.25},
    'sunflower': {'cost_per_m²': 0.56},
    'sweet potato': {'cost_per_m²': 4.0},
    'tangerine': {'cost_per_m²': 3.75},
    'tobacco': {'cost_per_m²': 0.2},
    'tomato': {'cost_per_m²': 12.5},
    'turnip': {'cost_per_m²': 2.4},
    'vanilla': {'cost_per_m²': 10.0},
    'walnut': {'cost_per_m²': 4.2},
    'watermelon': {'cost_per_m²': 1.05},
    'wheat': {'cost_per_m²': 0.14},
    'yam': {'cost_per_m²': 3.0},
    'zucchini': {'cost_per_m²': 5.25},
    'alfalfa': {'cost_per_m²': 0.5},
    'almond': {'cost_per_m²': 4.4},
    'amaranth': {'cost_per_m²': 1.5},
    'apple': {'cost_per_m²': 5.0},
    'apricot': {'cost_per_m²': 7.0},
    'artichoke': {'cost_per_m²': 3.75},
    'asparagus': {'cost_per_m²': 2.0},
    'avocado': {'cost_per_m²': 3.6},
    'banana': {'cost_per_m²': 0.5},
    'barley': {'cost_per_m²': 0.21},
    'basil': {'cost_per_m²': 15.0},
    'bean': {'cost_per_m²': 1.5},
    'beetroot': {'cost_per_m²': 4.2},
    'bell pepper': {'cost_per_m²': 10.0},
    'black gram': {'cost_per_m²': 1.5},
    'blackberry': {'cost_per_m²': 12.0},
    'blueberry': {'cost_per_m²': 7.5},
    'broccoli': {'cost_per_m²': 5.0},
    'buckwheat': {'cost_per_m²': 0.6},
   'cabbage': {'cost_per_m²': 2.25},
   'carrot': {'cost_per_m²': 3.0},
   'cantaloupe': {'cost_per_m²': 3.6},
   'cauliflower': {'cost_per_m²': 4.5},
   'celery': {'cost_per_m²': 3.0},
   'chickpea': {'cost_per_m²': 0.7},
   'chili pepper': {'cost_per_m²': 4.2},
   'clementine': {'cost_per_m²': 4.5},
   'coconut': {'cost_per_m²': 0.2},
   'corn': {'cost_per_m²': 0.75},
   'cranberry': {'cost_per_m²': 7.5},
   'cucumber': {'cost_per_m²': 7.2},
   'custard apple': {'cost_per_m²': 8.0},
   'date': {'cost_per_m²': 6.0},
   'dragon fruit': {'cost_per_m²': 15.0},
   'durian': {'cost_per_m²': 15.0},
   'elderberry': {'cost_per_m²': 7.5},
   'fennel': {'cost_per_m²': 8.0},
   'fig': {'cost_per_m²': 6.0},
   'flax': {'cost_per_m²': 0.8},
   'garlic': {'cost_per_m²': 5.0},
   'ginger': {'cost_per_m²': 4.5},
   'grape': {'cost_per_m²': 7.0},
   'grapefruit': {'cost_per_m²': 7.5},
   'green bean': {'cost_per_m²': 4.5},
   'guava': {'cost_per_m²': 6.0},
   'hemp': {'cost_per_m²': 0.5},
   'honeydew': {'cost_per_m²': 3.5},
   'jackfruit': {'cost_per_m²': 3.75},
   'jabuticaba': {'cost_per_m²': 12.0},
   'kale': {'cost_per_m²': 6.0},
   'kiwi': {'cost_per_m²': 5.0},
   'kohlrabi': {'cost_per_m²': 5.25},
   'kumquat': {'cost_per_m²': 8.0},
   'lavender': {'cost_per_m²': 40.0},
   'lemon': {'cost_per_m²': 3.0},
   'lentil': {'cost_per_m²': 0.6},
   'lettuce': {'cost_per_m²': 7.5},
    'lime': {'cost_per_m²': 1.8},
 'loquat': {'cost_per_m²': 10.0},
 'longan': {'cost_per_m²': 15.0},
 'lychee': {'cost_per_m²': 10.0},
 'mango': {'cost_per_m²': 6.25},
 'mandarin': {'cost_per_m²': 4.0},
 'mulberry': {'cost_per_m²': 12.0},
 'mung bean': {'cost_per_m²': 1.5},
 'mushroom': {'cost_per_m²': 12.5},
 'mustard': {'cost_per_m²': 1.2},
 'nectarine': {'cost_per_m²': 6.0},
 'okra': {'cost_per_m²': 3.0},
 'olive': {'cost_per_m²': 1.0},
 'onion': {'cost_per_m²': 4.0},
 'orange': {'cost_per_m²': 3.75},
 'oregano': {'cost_per_m²': 4.0},
 'papaya': {'cost_per_m²': 4.8},
 'parsnip': {'cost_per_m²': 4.5},
 'passion fruit': {'cost_per_m²': 8.75},
 'pea': {'cost_per_m²': 1.8},
 'peach': {'cost_per_m²': 5.0},
 'pear': {'cost_per_m²': 5.0},
 'peppermint': {'cost_per_m²': 4.5},
 'persimmon': {'cost_per_m²': 6.0},
 'pineapple': {'cost_per_m²': 5.0},
 'plum': {'cost_per_m²': 6.25},
    'pomegranate': {'cost_per_m²': 9.0},
    'potato': {'cost_per_m²': 1.35},
    'prickly pear': {'cost_per_m²': 4.0},
    'pumpkin': {'cost_per_m²': 5.0}}


# Extract cost_per_m² values into a simple dictionary for easier mapping
cost_data = {crop: details['cost_per_m²'] for crop, details in data2.items()}

# Read the existing CSV file
df = pd.read_csv('crop_finance.csv')

# Ensure 'cost_per_area' column exists, if not create it
df['cost_per_area'] = df['Crop'].map(cost_data)

# Replace NaN values with 0 or another placeholder if desired
df['cost_per_area'].fillna(0, inplace=True)

# Calculate cost_per_area as cost_per_m² * weight_area
df['cost_per_area'] = df['cost_per_area'] * df['weight_area']

# Save the updated DataFrame to a new CSV file
df.to_csv('crop_finance.csv', index=False)