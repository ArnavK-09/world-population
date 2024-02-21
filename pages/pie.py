# Imports 
from taipy.gui import Markdown
import pandas as pd

import random

# Our data file 
DATA = pd.read_csv("./data.csv")

# Excrating Pie Charts Data
pie_of_2022 = {
  "Country": list(DATA["Country/Territory"]),
  "Population": list(DATA["2022 Population"])
}

pie_of_2020 = {
  "Country": list(DATA["Country/Territory"]),
  "Population": list(DATA["2020 Population"])
}

pie_of_2015 = {
  "Country": list(DATA["Country/Territory"]),
  "Population": list(DATA["2015 Population"])
}

pie_of_2010 = {
  "Country": list(DATA["Country/Territory"]),
  "Population": list(DATA["2010 Population"])
}

pie_of_2000 = {
  "Country": list(DATA["Country/Territory"]),
  "Population": list(DATA["2000 Population"])
}

pie_of_1990 = {
  "Country": list(DATA["Country/Territory"]),
  "Population": list(DATA["1990 Population"])
}

pie_of_1980 = {
  "Country": list(DATA["Country/Territory"]),
  "Population": list(DATA["1980 Population"])
}

pie_of_1970 = {
  "Country": list(DATA["Country/Territory"]),
  "Population": list(DATA["1970 Population"])
}

# Pie configuration
pie_options = {
    # Hide the texts
    "textinfo": "none"
}


# Creating Page 
pie_page = Markdown("pie.md")