import pandas as pd
import requests
import csv
import time

# Step 1: Filtering Drug Repurposing Results
# Input: export.csv
# Output: Four separate CSV files for types 'cp', 'kd', 'oe', 'cc' with scores above 90

data = pd.read_csv('export.csv')

# Filtering rows based on Type and Score > 90
filtered_cp = data[(data['Type'] == 'cp') & (data['Score'] > 90)]
filtered_kd = data[(data['Type'] == 'kd') & (data['Score'] > 90)]
filtered_oe = data[(data['Type'] == 'oe') & (data['Score'] > 90)]
filtered_cc = data[(data['Type'] == 'cc') & (data['Score'] > 90)]

# Saving filtered data to new CSV files
filtered_cp.to_csv('filtered_cp_above_90.csv', index=False)
filtered_kd.to_csv('filtered_kd_above_90.csv', index=False)
filtered_oe.to_csv('filtered_oe_above_90.csv', index=False)
filtered_cc.to_csv('filtered_cc_above_90.csv', index=False)

print("CSV file 'filtered_cp_above_90.csv' created successfully.")
print("CSV file 'filtered_kd_above_90.csv' created successfully.")
print("CSV file 'filtered_oe_above_90.csv' created successfully.")
print("CSV file 'filtered_cc_above_90.csv' created successfully.")