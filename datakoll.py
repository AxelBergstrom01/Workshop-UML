import pandas as pd

# 1. Läs in dataset
df = pd.read_csv("osm_goteborg_pois.csv")

# 2. Hantera NaN
df = df.fillna("none")

# 3. Välj features
feature_cols = ["lat", "lon"]
X = df[feature_cols].copy()

# 4. Kolla att det funkar
print(X.head())

print(X.describe())