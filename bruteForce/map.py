import pandas as pd
from shapely.geometry import Point, geo
import geopandas as gpd
import matplotlib.pyplot as plt
from geopandas import GeoDataFrame
import time
import itertools
import pylab as pl
from matplotlib.text import TextPath

#Create a data frame from the results we save from the brute force method
df = pd.read_csv("resultsBruteForce.csv", delimiter=',', skiprows=0, low_memory=False)
#maps the points to a list of Point objects
geometry = [Point(xy) for xy in zip(df['Lat'], df['Long'])]
#Creates a Geodataframe out of points in order to put on map
gdf = GeoDataFrame(df, geometry=geometry) 
#this is a simple map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#plots the points with correct sizing
gdf.plot(ax=world.plot(figsize=(10, 6)),marker=(TextPath((0,0),"1")), color='red', markersize=50)
#Shows the map with the points on it
plt.show()