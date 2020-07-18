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

# Analyzing Features
# Now that your columns are ready, you want to see how different features of this dataset 
# relate to the quality rating of the wine. A very simple way you could do this is by observing 
# the mean quality rating for the top and bottom half of each feature. The code below does this 
# for four features. It looks pretty repetitive right now. Can you make this more concise?

median_alcohol = df.alcohol.median()
for i, alcohol in enumerate(df.alcohol):
    if alcohol >= median_alcohol:
        df.loc[i, 'alcohol'] = 'low'
df.groupby('alcohol').quality.mean()

#OUTPUT
alcohol
high    5.958904
low     5.310302
Name: quality, dtype: float64