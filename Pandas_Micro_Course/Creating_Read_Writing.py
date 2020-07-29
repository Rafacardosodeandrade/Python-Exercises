# 1. In the cell below, create a DataFrame fruits that looks like this:

# |Apples   |Bananas|
# |30       |21     |
# 
import pandas as pd
pd.set_option('max_rows', 5)

fruits = pd.DataFrame([[30, 21]], columns=['Apples' , 'Bananas'])
print(fruits)
