# 1. In the cell below, create a DataFrame fruits that looks like this:

# |Apples   |Bananas|
# |30       |21     |
# 
import pandas as pd
pd.set_option('max_rows', 5)

fruits = pd.DataFrame([[30, 21]], columns=['Apples' , 'Bananas'])
print(fruits)

#2. Create a dataframe fruit_sales that matches the diagram below:
#               |Apples   |Bananas|
# 2017 Sales    |30       |21     |
# 2018 Sales    |41       |34     |

fruit_sales = pd.DataFrame([[35, 21],[41, 34]], columns=['Apples','Bananas'], index=['2017 Sales', '2018 Sales'])
print(fruit_sales)

# 3. Create a variable ingredients with a Series that looks like:
#
# Flour     4 cups
# Milk       1 cup
# Eggs     2 large
# Spam       1 can
# Name: Dinner, dtype: object

quantities = ['4 cups', '1 cup','2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs', 'Spam']
recipe = pd.Series(quantities, index=items, name='Dinner')
ingredients = recipe
#print(ingredients)

# 4.Read the following csv dataset of wine reviews into a DataFrame called reviews:
# The filepath to the csv file is ../input/wine-reviews/winemag-data_first150k.csv. The first few lines look like:

reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)

# 5. Run the cell below to create and display a DataFrame called `animals`:
animals = pd.DataFrame({'Cows':[12, 20], 'Goats':[22, 19]}, index=['Year 1', 'Year 2'])
print(animals)



