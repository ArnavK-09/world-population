# Imports 
from taipy.gui import Markdown
import pandas as pd

# Our data file 
DATA = pd.read_csv("./data.csv")

# Selection Menus
CONTINENTS = list(DATA["Continent"].unique())
years_list = list(filter(lambda x: x.endswith("Population"), DATA.columns))
YEARS = list(map(lambda x: x.replace("Population", "").strip(), years_list))

# Choosen Value
continent = CONTINENTS[0]
year = YEARS[0]

# Chart content
chart_data = DATA.loc[DATA["Continent"]==continent].sort_values(by=[f"{year} Population"], ascending=False, ignore_index=True)[["Country/Territory", f"{year} Population"]].sort_values(by=f"{year} Population", ascending=False).head()

# On Year/Continent Selection!
def on_selection(state):
    year = state.year
    continent = state.continent
    state.chart_data = DATA.loc[DATA["Continent"]==continent].sort_values(by=[f"{year} Population"], ascending=False, ignore_index=True)[["Country/Territory", f"{year} Population"]].sort_values(by=f"{year} Population", ascending=False).head()

# Creating Page 
top_countries_in_continent = Markdown("top_countries_in_continent.md")