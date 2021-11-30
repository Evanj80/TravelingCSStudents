import pandas as pd
from shapely.geometry import Point, geo
import geopandas as gpd
import matplotlib.pyplot as plt
from geopandas import GeoDataFrame
import time

df = pd.read_csv("resultsBruteForce.csv", delimiter=',', skiprows=0, low_memory=False)

geometry = [Point(xy) for xy in zip(df['Lat'], df['Long'])]
gdf = GeoDataFrame(df, geometry=geometry)   

#this is a simple map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(10, 6)),marker='o', color='red', markersize=15)

plt.show()