# 1. Who are the most common wine reviewers in the dataset? Create a Series whose index 
# is the taster_twitter_handle category from the dataset, and whose values count how many 
# reviews each person wrote.

reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()






