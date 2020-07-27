from sklearn.ensemble import RandomForestRegressor
rf_model = RandomForestRegressor()

# Fit your model
rf_model.fit(train_X, train_y)

# Calculate the mean absolute error of your Random Forest Model on the validation data
rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

print("Validation MAE for Random Forest Model: {}".format(rf_val_mae))