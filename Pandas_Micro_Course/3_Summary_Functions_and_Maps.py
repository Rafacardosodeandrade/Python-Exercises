import pandas as pd 
pd.set_option("display_max_rows", 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.summary_functions_and_maps import *

# 1 What is the median of the points column in the reviews DataFrame?
median_points = reviews.points.median()
print(median_points)

# 2 What countries are represented in the dataset? (Your answer should not include any duplicates.)
countries = reviews.countries.unique()
print(countries)

# 3 How often does each country appear in the dataset? 
# Create a Series reviews_per_country mapping countries to the count of reviews of wines from that country.
reviews_per_country = reviews.country.value_count()
print(reviews_per_country)

# 4 Create variable centered_price containing a version of the price column with the mean price subtracted.
centered_price = reviews.price - reviews.price.mean()
print(centered_price)

# 5 I'm an economical wine buyer. Which wine is the "best bargain"? Create a variable bargain_wine
# with the title of the wine with the highest points-to-price ratio in the dataset.
bargain_idx = (reviews.points / reviews.price).idxmax
bargain_wine = reviews.loc[bargain_idx, 'title']

# 6 There are only so many words you can use when describing a bottle of wine.
# Is a wine more likely to be "tropical" or "fruity"? 
# Create a Series descriptor_counts counting how many times each of these two words appears in 
# the description column in the dataset.

n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
print(descriptor_counts)














