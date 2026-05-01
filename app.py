import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("/content/Unemployment in India.csv")

# Clean column names (important — spaces hoti hain)
df.columns = df.columns.str.strip()

# Check data
print(df.head())
print(df.info())

# Convert Date
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Extract Year & Month
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Remove missing values
df = df.dropna()

# 📊 1. Overall unemployment trend
plt.figure()
df.groupby('Date')['Estimated Unemployment Rate (%)'].mean().plot()
plt.title("Unemployment Rate Over Time (India)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.show()

# 📊 2. Year-wise trend
plt.figure()
df.groupby('Year')['Estimated Unemployment Rate (%)'].mean().plot(kind='bar')
plt.title("Year-wise Unemployment Rate (India)")
plt.xlabel("Year")
plt.ylabel("Rate (%)")
plt.show()

# 📊 3. COVID-19 Impact (2020)
covid = df[df['Year'] == 2020]

plt.figure()
covid.groupby('Month')['Estimated Unemployment Rate (%)'].mean().plot()
plt.title("COVID-19 Impact on Unemployment (2020)")
plt.xlabel("Month")
plt.ylabel("Rate (%)")
plt.show()

# 📊 4. State-wise unemployment
plt.figure()
df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values().plot(kind='bar')
plt.title("Unemployment by Region (India)")
plt.xlabel("Region")
plt.ylabel("Rate (%)")
plt.show()
