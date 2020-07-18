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

#   And here's a slightly better way you could do it. You can avoid making naming errors 
#   due to typos caused by manual typing. However, this looks a little repetitive. Can you make it better?
label = list(df.columns)
labels[0] = labels[0].replace('', '_')
labels[1] = labels[1].replace('', '_')
labels[2] = labels[2].replace('', '_')
labels[3] = labels[3].replace('', '_')
labels[4] = labels[4].replace('', '_')
labels[5] = labels[5].replace('', '_')
labels[6] = labels[6].replace('', '_')
df.columns = labels

df.head()
