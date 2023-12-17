import streamlit as st
import geopandas as gpd
import pandas as pd
import leafmap.foliumap as leafmap
from streamlit_extras.colored_header import colored_header
from utils.st_styles import init_styles
from utils.charts import pie_array, pie_array_ns, make_altair_bar

# Load the ACT shapefile
act_shapefile_path = "path_to_act_shapefile.shp"
act_data = gpd.read_file(act_shapefile_path)

# Load the census data for the ACT
census_data_path = "path_to_census_data.csv"
census_data = pd.read_csv(census_data_path)

# Merge the shapefile and census data
merged_data = act_data.merge(census_data, on="common_field")

# Create the interactive map
st.title("ACT Census Data Map")
st.map(merged_data)


