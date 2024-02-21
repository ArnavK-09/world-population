# Imports 
from taipy.gui import Markdown
import pandas as pd

# Our data file 
DATA = pd.read_csv("./data.csv")


# x: [1..5]
x_range = range(1, 6)
data = {
    "Countries": DATA["Country/Territory"],
    "Y": DATA["Growth Rate"],
}

# Creating Page 
dataset_page = Markdown("dataset.md")