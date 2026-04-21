import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

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

scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

print(X_scaled.describe())

minmax_scaler = MinMaxScaler()
X_minmax = pd.DataFrame(
    minmax_scaler.fit_transform(X),
    columns=X.columns
)

print(X_minmax.describe())