from art import text2art
string = "GalactoNet"
ascii_art = text2art(string)
print("=" * 60)
print(" ")
print(ascii_art)
print("=" * 60)
print("                 Welcome to GalactoNet!")
print("GalactoNet is a tool to visualize pathogens across the US.")
print("   It is built and maintained by the Galacto Corp. team.")
print("=" * 60)
print(" ")

from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv(r"C:\Users\Danie\OneDrive\Desktop\GalactoNet\file.csv",
                   dtype={"fips": str})

fig = px.choropleth(df, geojson=counties, locations='fips', color='conc.',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           scope="usa",
                           labels={'Avg. Conc. / Sample':'Klebsiella Pneumoniae Concentration'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
