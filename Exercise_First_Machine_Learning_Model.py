# Exercise made on KAGGLE.COM 
#
# Step 1: Specify Prediction Target
# Select the target variable, which corresponds to the sales price.
# Save this to a new variable called y. 
# You'll need to print a list of the columns to find the name of the column you need.

# print the list of columns in the dataset to find the name of the prediction target
print(home_data)

        Id  MSSubClass MSZoning  LotFrontage  LotArea Street Alley LotShape  \
0        1          60       RL         65.0     8450   Pave   NaN      Reg   
1        2          20       RL         80.0     9600   Pave   NaN      Reg   
2        3          60       RL         68.0    11250   Pave   NaN      IR1   
3        4          70       RL         60.0     9550   Pave   NaN      IR1   
4        5          60       RL         84.0    14260   Pave   NaN      IR1   
...    ...         ...      ...          ...      ...    ...   ...      ...   
1455  1456          60       RL         62.0     7917   Pave   NaN      Reg   
1456  1457          20       RL         85.0    13175   Pave   NaN      Reg   
1457  1458          70       RL         66.0     9042   Pave   NaN      Reg   
1458  1459          20       RL         68.0     9717   Pave   NaN      Reg   
1459  1460          20       RL         75.0     9937   Pave   NaN      Reg   

     LandContour Utilities  ... PoolArea PoolQC  Fence MiscFeature MiscVal  \
0            Lvl    AllPub  ...        0    NaN    NaN         NaN       0   
1            Lvl    AllPub  ...        0    NaN    NaN         NaN       0   
2            Lvl    AllPub  ...        0    NaN    NaN         NaN       0   
3            Lvl    AllPub  ...        0    NaN    NaN         NaN       0   
4            Lvl    AllPub  ...        0    NaN    NaN         NaN       0   
...          ...       ...  ...      ...    ...    ...         ...     ...   
1455         Lvl    AllPub  ...        0    NaN    NaN         NaN       0   
1456         Lvl    AllPub  ...        0    NaN  MnPrv         NaN       0   
1457         Lvl    AllPub  ...        0    NaN  GdPrv        Shed    2500   
1458         Lvl    AllPub  ...        0    NaN    NaN         NaN       0   
1459         Lvl    AllPub  ...        0    NaN    NaN         NaN       0   

     MoSold YrSold  SaleType  SaleCondition  SalePrice  
0         2   2008        WD         Normal     208500  
1         5   2007        WD         Normal     181500  
2         9   2008        WD         Normal     223500  
3         2   2006        WD        Abnorml     140000  
4        12   2008        WD         Normal     250000  
...     ...    ...       ...            ...        ...  
1455      8   2007        WD         Normal     175000  
1456      2   2010        WD         Normal     210000  
1457      5   2010        WD         Normal     266500  
1458      4   2010        WD         Normal     142125  
1459      6   2008        WD         Normal     147500  

[1460 rows x 81 columns]

y = home_data['SalePrice']

# Step 2: Create X
# Now you will create a DataFrame called X holding the predictive features.
#
# Since you want only some columns from the original data, you'll first
# create a list with the names of the columns you want in X.
#
# You'll use just the following columns in the list (you can copy and paste
# the whole list to save some typing, though you'll still need to add quotes):
#
# * LotArea
# * YearBuilt
# * 1stFlrSF
# * 2ndFlrSF
# * FullBath
# * BedroomAbvGr
# * TotRmsAbvGrd
#
# After you've created that list of features, use it to create the DataFrame
# that you'll use to fit the model.
#
# Create the list of features below 
feature_names = ['LotArea','YearBuilt','1stFlrSF', '2ndFlrSF', 'FullBath','BedroomAbvGr','TotRmsAbcGrd']
# Select data corresponding to features in feature_names
X = home_data[feature_names]

# Review Data
#
# Before building a model, take a quick look at X to verify it looks sensible
#
# Review Data
# Print description or satatistics from X
X.describe()
# Print the top few lines
X.head()
#
# Step 3: Specify and Fit Model
# Create a DecisionTreeRegressor and save it iowa_model. 
# Ensure you've done the relevant import from sklearn to run this command.
#
# Then fit the model you just created using the data in X and y that you saved above.
from sklear.tree import DecisionTreeRegressor
# For model reproducibility, set a numeric value for random_state when specifying the model
iowa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(X,y)
#
# Step 4: Make Predictions
# Make predictions with the model's predict command using X as the data.
# Save the results to a variable called predictions.
predictions = iowa_model.predict(X)
print(predictions)
#OUTPUT
[208500. 181500. 223500. ... 266500. 142125. 147500.]

#MODEL VALIDATION
#
# You'll want to evaluate almost every model you ever build. 
# In most (though not all) applications, the relevant measure of model quality is predictive accuracy.
# In other words, will the model's predictions be close to what actually happens.
# Many people make a huge mistake when measuring predictive accuracy. 
# They make predictions with their training data and compare those predictions to the target 
# values in the training data. You'll see the problem with this approach and how to solve it in a 
# moment, but let's think about how we'd do this first.
# You'd first need to summarize the model quality into an understandable way.
# If you compare predicted and actual home values for 10,000 houses, you'll likely find mix of good 
# and bad predictions. Looking through a list of 10,000 predicted and actual values would be pointless. 
# We need to summarize this into a single metric. 
# There are many metrics for summarizing model quality, but we'll start with one called 
# Mean Absolute Error (also called MAE). Let's break down this metric starting with the last word, error.
# The prediction error for each house is:

error = actual-predicted

# i.e

import pandas as pd 

#Load data
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 

# Filter rows with missing price values
filtered_melbourne_data = melbourne_data.dropna(axis=0)

# Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms','Bathroom','Landsize','BuildingArea', 'YearBuilt'.'Lattitude', 'Longitude']

X = filtered_melbourne_data[melbourne_features]

from sklearn.tree import DecisionTreeRegressor
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(X, y)

# Once we have a model, here is how we calculate the mean absolute error:

from sklearn.metrics import mean_ansolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)

# OUTPUT
434.71594577146544

# The Problem with "In-Sample" Scores
# The measure we just computed can be called an "in-sample" score. We used a single "sample" of
# houses for both building the model and evaluating it. Here's why this is bad.
# 
# Imagine that, in the large real estate market, door color is unrelated to home price.
# However, in the sample of data you used to build the model, all homes with green doors 
# were very expensive. The model's job is to find patterns that predict home prices, so it will
# see this pattern, and it will always predict high prices for homes with green doors.
#
# Since this pattern was derived from the training data, the model will appear accurate in the training data.
#
# But if this pattern doesn't hold when the model sees new data, the model would be very 
# inaccurate when used in practice.
#
# Since models' practical value come from making predictions on new data, we measure performance on 
# data that wasn't used to build the model. The most straightforward way to do this is to exclude some 
# data from the model-building process, and then use those to test the model's accuracy on data it
#  hasn't seen before. This data is called validation data.
#
#
#
# Coding It
# The scikit-learn library has a function train_test_split to break up the data into two pieces. 
# We'll use some of that data as training data to fit the model, and we'll use the other data as
# validation data to calculate mean_absolute_error.
#
# Here is the code:
from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we run this script:
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_ansolute_error(val_y, val_predictions))

#OUTPUT
260991.8108457069

# Your mean absolute error for the in-sample data was about 500 dollars. Out-of-sample
# it is more than 250,000 dollars.
#
# This is the difference between a model that is almost exactly right, and one that is unusable
# for most practical purposes. As a point of reference, the average home value in the validation
# data is 1.1 million dollars. So the error in new data is about a quarter of the average home value.














