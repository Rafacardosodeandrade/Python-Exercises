# 1. What is the data type of the points column in the dataset?
dtype = reviews.point.dtype 

# 2. Create a Series from entries in the points column, but convert the entries to strings. Hint: strings are str in native Python.
point_strings = reviews.points.astype(str)