import pandas as pd

# Ladda dataset
df = pd.read_csv("osm_goteborg_pois.csv")

print("=== INFO ===")
print(df.info())

print("\n=== BESKRIVNING ===")
print(df.describe())

df = df.fillna("none")

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== HEAD ===")
print(df.head())

feature_cols = ["lat", "lon"]
X = df[feature_cols].copy()feature_cols = ["lat", "lon"]
