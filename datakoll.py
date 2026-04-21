import pandas as pd

# Ladda dataset
df = pd.read_csv("osm_goteborg_pois.csv")

print("=== INFO ===")
print(df.info())

print("\n=== BESKRIVNING ===")
print(df.describe())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

df = df.fillna("none")

print("\n=== HEAD ===")
print(df.head())