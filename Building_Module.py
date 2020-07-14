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
melbourne_model = DecisionTreeRegressor(random_state=1) #  exposes a number of methods 
# for generating random numbers drawn from a variety of probability distributions.





