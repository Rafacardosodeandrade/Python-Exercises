# 1. Who are the most common wine reviewers in the dataset? Create a Series whose index 
# is the taster_twitter_handle category from the dataset, and whose values count how many 
# reviews each person wrote.

reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()

# 2. What is the best wine I can buy for a given amount of money? Create a Series whose 
# index is wine prices and whose values is the maximum number of points a wine costing 
# that much was given in a review. Sort the values by price, ascending (so that 4.0 dollars 
# is at the top and 3300.0 dollars is at the bottom).






