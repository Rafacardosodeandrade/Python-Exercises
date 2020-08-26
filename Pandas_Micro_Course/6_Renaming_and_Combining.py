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

# The [Things on Reddit](https://www.kaggle.com/residentmario/things-on-reddit/data) dataset 
# includes product links from a selection of top-ranked forums ("subreddits") on reddit.com. 
# Run the cell below to load a dataframe of products mentioned on the */r/gaming* subreddit 
# and another dataframe for products mentioned on the *r//movies* subreddit.

gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"

# Create a `DataFrame` of products mentioned on *either* subreddit.

combine_products = pd.concat([gaming_products, movie_products])

