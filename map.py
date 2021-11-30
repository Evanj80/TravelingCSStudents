import pandas as pd
from shapely.geometry import Point, geo
import geopandas as gpd
import matplotlib.pyplot as plt
from geopandas import GeoDataFrame
import time
import itertools
import pylab as pl
from matplotlib.text import TextPath

i=0
def increment():
    return str(i + 1)

df = pd.read_csv("resultsBruteForce.csv", delimiter=',', skiprows=0, low_memory=False)

geometry = [Point(xy) for xy in zip(df['Lat'], df['Long'])]
gdf = GeoDataFrame(df, geometry=geometry) 
marker = itertools.cycle(tuple(range(1, 101)))
print(marker)

#this is a simple map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(10, 6)),marker=(TextPath((0,0),str(next(marker)))), color='red', markersize=50)


plt.show()