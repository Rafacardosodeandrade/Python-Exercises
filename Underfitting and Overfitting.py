# Code you have used to load the data 
import pandas as pd 
from sklearn.metrics import mean_absolute_error
from sklear.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Path of this file
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

home_data = pd.read_csv(iowa_file_path)
# Create target object and call it y
y = home_data.SalesPrice
# Create X
features = ['LotArea','YearBuilt', '1stFlrSF', '2ndFlorSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[features]

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Specify model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit model
iowa_model.fit(train_X, train_y)

# Make Validation predictions and calculate mean absolute error
val_predictions = iowa_model_predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE: {:,.0f}".format(val_mae))
#OUTPUT
Validation MAE: 29,653

###
###
### EXERCISIE ###
#################
# Step 1: Compare Different Tree Sizes
# Write a loop that tries the following values for max_leaf_nodes from a 
# set of possible values.

# Call the get_mae function on each value of max_leaf_nodes. Store the output 
# in some way that allows you to select the value of max_leaf_nodes that gives 
# the most accurate model on your data.

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
# Loop to find the ideal tree size from candidate_max_leaf_nodes
for max_leaf_nodes in candidate_max_leaf_nodes:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d \t\t Mean Absolute Error:   %d"  %(max_leaf_nodes, my_mae)) 

# Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate max_leaf_nodes}
print("\n", scores)

best_tree_size = min(scores, key=scores.get)

print("\n", best_tree_size, scores[best_tree_size])

# OUTPUT
Max leaf nodes: 5  		     Mean Absolute Error:  35044
Max leaf nodes: 25  		 Mean Absolute Error:  29016
Max leaf nodes: 50  		 Mean Absolute Error:  27405
Max leaf nodes: 100  		 Mean Absolute Error:  27282
Max leaf nodes: 250  		 Mean Absolute Error:  27893
Max leaf nodes: 500  		 Mean Absolute Error:  29454

 {5: 35044.51299744237, 25: 29016.41319191076, 50: 27405.930473214907, 100: 27282.50803885739, 250: 27893.822225701646, 500: 29454.18598068598}

 100 27282.50803885739
 


###### Step 2: Fit Model Using All Data
# You know the best tree size. If you were going to deploy this model in practice, 
# you would make it even more accurate by using all of the data and keeping that tree size.
# That is, you don't need to hold out the validation data now that you've made all your 
# modeling decisions.
# # # 

# argument to make optimal size and uncomment
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=1)

# fit the final model and uncomment the next two lines
final_model.fit(X, y)


