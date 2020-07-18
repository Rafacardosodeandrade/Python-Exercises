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

#THE BEST MODE
df.colums = [label.replace(' ', '_') for label in df.columns]
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

median_pH = df.pH.median()
for i, pH in enumerate(df.pH):
    if pH >= median_pH:
        df.loc[i, 'pH'] = 'high'
    else:
        df.loc[i, 'pH'] = 'low'
df.groupby('pH').quality.mean()
#OUTPUT
pH
high    5.598039
low     5.675607
Name: quality, dtype: float64

median_sugar = df.residual_sugar.median()
for i, sugar in enumerate(df.residual_sugar):
    if sugar >= median_sugar:
        df.loc[i, 'residual_sugar'] = 'high'
    else:
        df.loc[i, 'residual_sugar'] = 'low'
df.groupby('residual_sugar').quality.mean()
#OUTPUT
residual_sugar
high    5.665880
low     5.602394
Name: quality, dtype: float64

median_citric_acid = df.citric_acid.median()
for i, citric_acid in enumerate(df.citric_acid):
    if citric_acid >= median_citric_acid:
        df.loc[i, 'citric_acid'] = 'high'
    else:
        df.loc[i, 'citric_acid'] = 'low'
df.groupby('citric_acid').quality.mean()
#OUTPUT
citric_acid
high    5.822360
low     5.447103
Name: quality, dtype: float64

#BEST METHOD

def numeric_for_busckets(df, column_name):
    median = df[column_name].median()
    for i, val in enumerate(df[column_name]):
        if val >= median:
            df.loc[i, column_name] = 'high'
        else:
            df.loc[i, column_name] = 'low'

for feature in df.columns[:-1]:
    numeric_for_busckets(df, feature)
    print(df.groupby(feature).quality.mean(), '\n')