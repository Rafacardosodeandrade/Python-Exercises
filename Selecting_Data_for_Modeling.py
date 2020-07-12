# This is a exemplo made by Kaggle.com - it's very important to show step by step how Select Data for Modeling.
# 
# SELECTING DATA FOR MODELING
# Your dataset had too many variables to wrap your head around, or even to print out nicely. 
# How can you pare down this overwhelming amount of data to something you can understand?
# To choose variables/columns, we'll need to see a list of all columns in the dataset.
# That is done with the columns property of the DataFrame (the bottom line of code below).

#step 1: import PANDAS (specific library to manipulate Dataframes) and bring dataframe (csv file).
#the name of DATAFRAME is melbourne
import pandas as pd 

melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv' #bring data
melbourne_data = pd.read_csv(melbourne_file_path) #reading data
melbourne_data.columns #reading columns titles


