# Building Your Model
#
# You will use the scikit-learn library to create your models. 
# When coding, this library is written as sklearn, as you will see in the sample code.
# Scikit-learn is easily the most popular library for modeling the types of data 
# typically stored in DataFrames.
#
# 1. Define: What type of model will it be? A decision tree? 
# Some other type of model? Some other parameters of the model type are specified too.
# 2. Fit: Capture patterns from provided data. This is the heart of modeling.
# 3. Predict: Just what it sounds like
# 4. Evaluate: Determine how accurate the model's predictions are.
#
from sklearn.tree import DecisionTreeRegressor

# Define model.
# Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)  # exposes a number of methods for generating random numbers drawn from a variety of probability distributions.

# Fit model
melbourne_model.fit(X, y)
# OUTPUT - File originally made in Jupyter Notebook
DecisionTreeRegressor(criterion='mse', max_depth=None, max_features=None,
                      max_leaf_nodes=None, min_impurity_decrease=0.0,
                      min_impurity_split=None, min_samples_leaf=1,
                      min_samples_split=2, min_weight_fraction_leaf=0.0,
                      presort=False, random_state=1, splitter='best')

# Many machine learning models allow some randomness in model training. 
# Specifying a number for random_state ensures you get the same results in each run. 
# This is considered a good practice. You use any number, and model quality won't 
# depend meaningfully on exactly what value you choose.
#
# We now have a fitted model that we can use to make predictions.
# 
# In practice, you'll want to make predictions for new houses coming on the market 
# rather than the houses we already have prices for. But we'll make predictions for
# the first few rows of the training data to see how the predict function works.


print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))

#OUTPUT
Making predictions for the following 5 houses:
   Rooms  Bathroom  Landsize  Lattitude  Longtitude
1      2       1.0     156.0   -37.8079    144.9934
2      3       2.0     134.0   -37.8093    144.9944
4      4       1.0     120.0   -37.8072    144.9941
6      3       2.0     245.0   -37.8024    144.9993
7      2       1.0     256.0   -37.8060    144.9954
The predictions are
[1035000. 1465000. 1600000. 1876000. 1636000.]

# DONE 



