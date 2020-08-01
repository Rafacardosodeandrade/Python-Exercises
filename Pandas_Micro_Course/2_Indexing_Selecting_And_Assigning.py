import pandas as pd 
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# Look at an overview of your data by running the following line.
reviews.head()

# EXERCISES
# 1. Select the `description` column from `reviews` and assign the result to the variable `desc`.

desc = reviews['description']