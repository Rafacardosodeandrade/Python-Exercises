# You will work with data from the Housing Prices Competition for Kaggle Learn 
# Users to predict home prices in Iowa using 79 explanatory variables describing 
# (almost) every aspect of the homes.

# Run the next code cell without changes to load the training and validation features 
# in X_train and X_valid, along with the prediction targets in y_train and y_valid. 
# The test features are loaded in X_test. (If you need to review features and prediction targets,
#  please check out this short tutorial. To read about model validation, look here. 
# Alternatively, if you'd prefer to look through a full course to review all of these topics, start here.)

import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
X_full = pd.read_csv('../input/train.csv', index_col='Id')
X_test_full = pd.read_csv('../input/test.csv', index_col='Id')

# Obtain target and predictors
y = X_full.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = X_full[features].copy()
X_test = X_test_full[features].copy()

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                      random_state=0)


