import pandas as pd 
df = pd.read_csv ('winequality-red.csv', sep=';')
df.head()

#   Renaming Column
new_df = df.rename(columns)={'fixed acidity': 'fixed_acidity',
                             'volatile acidity': 'volatile_acidity',
                             'citric acid': 'citric_acid',
                             'residual sugar': 'residual_sugar',
                             'free sulfur dioxide': 'free_sulfur_dioxide',
                             'total sulfur dioxide': 'total_sulfur_dioxide'
                            })
new_df.head()