# UNEMPLOYMENT ANALYSIS

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("unemployment.csv")

# Clean
df = df.dropna()

# Convert date if exists
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])

# Plot
plt.figure()
plt.plot(df['Date'], df['Unemployment_Rate'])
plt.title("Unemployment Trend")
plt.xlabel("Date")
plt.ylabel("Rate")
plt.show()

# Insights
print("Average Unemployment Rate:", df['Unemployment_Rate'].mean())
print("Max Rate:", df['Unemployment_Rate'].max())
