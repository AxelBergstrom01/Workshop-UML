import osmnx as ox

tags = {
    "amenity": True,
    "leisure": True,
    "shop": True
}

place = {
    "city": "Göteborg",
    "country": "Sweden"
}

gdf = ox.features_from_place(place, tags)

gdf = gdf[gdf.geometry.type == "Point"]
gdf["lon"] = gdf.geometry.x
gdf["lat"] = gdf.geometry.y

df = gdf[["lat", "lon", "amenity", "leisure", "shop"]]
df.to_csv("osm_goteborg_pois.csv", index=False)

print("Antal rader:", len(df))
print("KLART!")