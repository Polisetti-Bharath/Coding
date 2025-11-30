import pandas as pd
import numpy as np

df = pd.read_csv(r"D:/Study/Coding/College/Python/temperature.csv")
print("CSV Columns:", df.columns)
print("\nFirst few rows:")
print(df.head())

# Parse 'date' column
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Use correct temperature column name
temp_col = 'temperature_celsius'  # <-- change this based on your CSV

# Handle missing temperature values
df[temp_col] = df[temp_col].fillna(df[temp_col].mean())

# Add Fahrenheit column
df['temperature_fahrenheit'] = df[temp_col] * 9/5 + 32

# 7-day rolling average
df['temp_7day_avg'] = df[temp_col].rolling(window=7, min_periods=1).mean()

# Normalize temperature (Min-Max)
temp_min = df[temp_col].min()
temp_max = df[temp_col].max()
df['temp_normalized'] = (df[temp_col] - temp_min) / (temp_max - temp_min)

# Save transformed data
output_path = r"D:/Study/Coding/College/Python/temperature_transformed.csv"
df.to_csv(output_path, index=False)
print(f"\nTransformed data saved to: {output_path}")
