# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:24:10 2024

@author: belinfo
"""

import csv

# Specify the path to your CSV file
csv_file_path = 'finance_data.csv'

# Specify the column name you want to print
column_name = 'Crop'

# Open the CSV file
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)

    # Print the contents of the specified column
    for row in csv_reader:
        print(row[column_name])
