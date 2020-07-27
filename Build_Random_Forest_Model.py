# Build a Random Forest model and train it on all of X and y.

# To improve accuracy, create a new Random Forest model with you will train on all training data
rf_model_on_full_data = RandomForestRegressor(random_state=1)

# Fit rf_model_on_full_data on all data from the
rf_model_on_full_data.fit(train_X, train_y)