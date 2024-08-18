
import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
input_file = 'primary.csv'  # Replace with your input file path
df = pd.read_csv(input_file)

# Initialize a list to collect the output data
output_data = []

# Process each row in the DataFrame
for index, row in df.iterrows():
    crop = row['Crop']
    
    # Generate 50 lines of different parameters for each crop
    for _ in range(1000):
        ph = np.random.uniform(row['MinPH'], row['MaxPH'])
        temp = np.random.uniform(row['MinTemp'], row['MaxTemp'])
        rain = np.random.uniform(row['MinRain'], row['MaxRain'])
        humidity = np.random.uniform(row['MinHumidity'], row['MaxHumidity'])
        n = np.random.uniform(row['MinN'], row['MaxN'])
        p = np.random.uniform(row['MinP'], row['MaxP'])
        k = np.random.uniform(row['MinK'], row['MaxK'])
        
        # Append the generated values to the output data list
        output_data.append([crop, ph, temp, rain, humidity, n, p, k])

# Convert the list to a DataFrame
output_df = pd.DataFrame(output_data, columns=['Crop', 'pH', 'Temp', 'Rain', 'Humidity', 'Nitrogen', 'Phosphorus', 'Potassium'])

# Save the output DataFrame to a CSV file
output_file = 'trainable_data.csv'  
output_df.to_csv(output_file, index=False)

print(f'Output has been saved to {output_file}')
