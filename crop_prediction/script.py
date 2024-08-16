import pandas as pd

# Update the path to the location of your datatired.csv file
input_file = 'datatired.csv'
output_file = 'C:/Users/belinfo/Desktop/agri_ai/finance_data.csv'

# Read the CSV file
df = pd.read_csv('datatired.csv')

# Extract the 'Crop' column and remove duplicates
unique_crops = df[['Crop']].drop_duplicates()

# Save the unique crops to a new CSV file
unique_crops.to_csv(output_file, index=False)

print(f"CSV file '{output_file}' has been created with unique crop names.")
