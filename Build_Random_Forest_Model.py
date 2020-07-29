# Build a Random Forest model and train it on all of X and y.

# To improve accuracy, create a new Random Forest model with you will train on all training data
rf_model_on_full_data = RandomForestRegressor(random_state=1)

# Fit rf_model_on_full_data on all data from the
rf_model_on_full_data.fit(X, y)

#Make Predictions
Read the file of "test" data. And apply your model to make predictions

# path to file you will use for predictions
test_data_path = '../input/test.csv'

# read test data file using pandas
test_data = pd.read_csv(test_data_path)

# create test_X which comes from test_data but includes only the columns you used for prediction.
# The list of columns is stored in a variable called features
test_X = test_data[features]


# make predictions which we will submit.
test_preds = rf_model_on_full_data.predict(test_X)

# The lines below shows you how to save your data in the format needed to score it in the competition






