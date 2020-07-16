# Code you have previously used to load data

import pandas as pd 
from sllearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

home_data = pd.read_csv(iowa_file_path)
y = home_data.SalesPrice
feature_columns = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_columns]

# Specify Model
iowa_model = DecisionTreeRegressor()
# Fit Model
iowa_model.fit(X, y)

print("First in-sample predictions:", iowa_model.predict(X.head()))
print("Actual target values for those homes:", y.head().tolist())

#OUTPUT
First in-sample predictions: [208500. 181500. 223500. 140000. 250000.]
Actual target values for those homes: [208500, 181500, 223500, 140000, 250000]

##########################################################################################
# #########################################################################################
#   STEP 1
#   Split Your Data
#
#   Use the train_test_split function to split up your data.
#   Give it the argument random_state=1 so the check functions know what to expect when verifying your code.
#   Recall, your features are loaded in the DataFrame X and your target is loaded in y.
#
from sklearn.model_selection import train_test_split # Import
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
#
#
#   STEP 2
#   Create a `DecisionTreeRegressor` model and fit it to the relevant data.
#   Set `random_state` to 1 again when creating the model.
#
# IMPORTANT: You imported DecisionTreeRegressor in your last exercise
# and that code has been copied to the setup code above. So, no need to
# import it again
#
#   Specify the model
iowa_model = DecisionTreeRegressor(random_state=1)
#   Fit the model with training data
iowa_model.fit(train_X, train_y)
#
# OUTPUT
[186500. 184000. 130000.  92000. 164500. 220000. 335000. 144152. 215000.
 262000.]
[186500. 184000. 130000.  92000. 164500. 220000. 335000. 144152. 215000.
 262000.]
 








