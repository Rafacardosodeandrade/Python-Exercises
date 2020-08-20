# Question 1
# Scikit-learn works with lists, numpy arrays, scipy-sparse matrices, and pandas DataFrames, so converting the dataset to a DataFrame is not necessary for training this model. Using a DataFrame does however help make many things easier such as munging data, so let's practice creating a classifier with a pandas DataFrame.

# Convert the sklearn.dataset cancer to a DataFrame.

# This function should return a (569, 31) DataFrame with

# columns =

['mean radius', 'mean texture', 'mean perimeter', 'mean area',
'mean smoothness', 'mean compactness', 'mean concavity',
'mean concave points', 'mean symmetry', 'mean fractal dimension',
'radius error', 'texture error', 'perimeter error', 'area error',
'smoothness error', 'compactness error', 'concavity error',
'concave points error', 'symmetry error', 'fractal dimension error',
'worst radius', 'worst texture', 'worst perimeter', 'worst area',
'worst smoothness', 'worst compactness', 'worst concavity',
'worst concave points', 'worst symmetry', 'worst fractal dimension',
'target']
# and index =

# RangeIndex(start=0, stop=569, step=1)

def answer_one():
    df=pd.DataFrame(cancer.data, columns=cancer.feature_names)
    df['target']=cancer.target
    return df


# Question 2
# What is the class distribution? (i.e. how many instances of malignant (encoded 0) and how many benign (encoded 1)?)

# This function should return a Series named target of length 2 with integer values and index = ['malignant', 'benign']

def answer_two():
    cancerdf = answer_one()
    Distribution=pd.Series([len(cancerdf[cancerdf['target']==0]),len(cancerdf[cancerdf['target']==1])],name='target',index=['malignant','benign'])
    return Distribution

# Question 3
# Split the DataFrame into X (the data) and y (the labels).

# This function should return a tuple of length 2: (X, y), where

# X, a pandas DataFrame, has shape (569, 30)
# y, a pandas Series, has shape (569,).
