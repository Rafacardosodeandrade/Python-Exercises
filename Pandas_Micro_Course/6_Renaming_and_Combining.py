import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.renaming_and_combining import *
print("Setup complete.")

Exercises
# View the first several lines of your data by running the cell below:
reviews.head()

# 1. region_1 and region_2 are pretty uninformative names for locale columns in the dataset. 
# Create a copy of reviews with these columns renamed to region and locale, respectively.
renamed = reviews.rename(columns=dict(region_1='region', region_2='locale'))

# 2. Set the index name in the dataset to wines.
reindex = reviews.rename_axis('wines', axis='rows')

