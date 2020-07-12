# This is a exemplo made by Kaggle.com - it's very important to show step by step how Select Data for Modeling.
# 
# SELECTING DATA FOR MODELING
# Your dataset had too many variables to wrap your head around, or even to print out nicely. 
# How can you pare down this overwhelming amount of data to something you can understand?
# To choose variables/columns, we'll need to see a list of all columns in the dataset.
# That is done with the columns property of the DataFrame (the bottom line of code below).

# step 1: import PANDAS (specific library to manipulate Dataframes) and bring dataframe (csv file).
# the name of DATAFRAME is melbourne
import pandas as pd 

melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv' #bring data
melbourne_data = pd.read_csv(melbourne_file_path) #reading data
melbourne_data.columns #reading columns titles

# OUTPUT - This scripts was made in Jupyter Notebooks (copy and paste)
Index(['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG',
       'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car',
       'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude',
       'Longtitude', 'Regionname', 'Propertycount'],
      dtype='object')

# The Melbourne data has some missing values (some houses for which some variables weren't recorded.)
# So we will take the simplest option for now, and drop houses from our data. 

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

# There are many ways to select a subset of your data.
# "Dot notation", which we use to select the "prediction target"
# Selecting with a column list, which we use to select the "features"

# SELECTING THE PREDICTION TARGET
# We'll use the dot notation to select the column we want to predict, which is called the prediction target.
# By convention, the prediction target is called y. So the code we need to save the house prices in the Melbourne data is
y = melbourne_data.Price 

