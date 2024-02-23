# Imports 
from taipy.gui import Markdown
import pandas as pd

# Our data file 
DATA = pd.read_csv("./data.csv")

# All Countries List 
COUNTRIES = list(DATA["Country/Territory"].unique())

# Chosen Values  
country1 = COUNTRIES[0]
country2 = COUNTRIES[1]

# Selection Handler for Country 1
def choose_country1(state):
    country1 = state.country1

# Selection Handler for Country 2
def choose_country2(state):
    country2 = state.country2 

# Creating Page 
compare_countries_page = Markdown("compare_countries.md")