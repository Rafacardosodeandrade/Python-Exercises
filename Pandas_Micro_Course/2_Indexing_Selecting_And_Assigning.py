import pandas as pd 
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# Look at an overview of your data by running the following line.
reviews.head()

# EXERCISES
# 1. Select the `description` column from `reviews` and assign the result to the variable `desc`.
desc = reviews['description']

# 2. Select the first value from the description column of reviews, assigning it to variable first_description.
first_description = reviews.description[0]

# 3. Select the first row of data (the first record) from reviews, assigning it to the variable first_row.
first_row = reviews.iloc[0]

# 4. Select the first 10 values from the description column in reviews, assigning the result to variable first_descriptions.
# Hint: format your output as a pandas Series.
first_description = reviews.description[:10]

# 5 Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.
# In other words, generate the following DataFrame:
indices = [1, 2, 3, 5, 8]
sample_reviews= reviews.loc[indices]



