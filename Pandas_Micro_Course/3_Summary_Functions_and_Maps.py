import pandas as pd 
pd.set_option("display_max_rows", 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# 1 What is the median of the points column in the reviews DataFrame?
median_points = reviews.points.median()

# 2 What countries are represented in the dataset? (Your answer should not include any duplicates.)
countries = reviews.countries.unique()