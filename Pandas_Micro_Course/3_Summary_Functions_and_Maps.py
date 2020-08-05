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
centered_price = reviews.price