# Step 1: Loading Data
# Read the Iowa data file into a Pandas DataFrame called home_data.

import pandas as pd 
# Path of the file to read
iowa_file_path = '.../input/home-data-for-ml-course/train.csv'
# Fill in the line below to read the file into a variable home_data
home_data = pd.read_csv(iowa_file_path)

# Step 2: Review The Data
# Use the command you learned to view summary statistics of the data.
# Then fill in variables to answer the following questions

# Print summary statistics in next line
home_data.describe()
# OUTPUT - DATAFRAME

# What is the average lot size (rounded to nearest integer)?
avg_lot_size = round(home_data['LotArea'].mean())


