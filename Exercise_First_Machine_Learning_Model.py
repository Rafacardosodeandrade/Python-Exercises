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












