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

def answer_three()
    cancerdf = answer_one()
    X=cancerdf[cancer['feature_names']]
    y=cancerdf['target']

    return X, y

answer_three()

# Question 4
# Using train_test_split, split X and y into training and test sets (X_train, 
# X_test, y_train, and y_test).

# Set the random number generator state to 0 using random_state=0 to make sure 
# your results match the autograder!

# This function should return a tuple of length 4: (X_train, X_test, y_train, y_test)
# , where

X_train has shape (426, 30)
X_test has shape (143, 30)
y_train has shape (426,)
y_test has shape (143,)

from sklearn.model_selection import train_test_split

def answer_four():
    X,y=answer_three()

    X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)

    return X_train,X_test,y_train,y_test

answer_four()

# 5. Using KNeighborsClassifier, fit a k-nearest neighbors (knn) classifier with X_train, 
# y_train and using one nearest neighbor (n_neighbors = 1).

# This function should return a sklearn.neighbors.classification.KNeighborsClassifier.

from sklearn.neighbors import KNeighborsClassifier

def answer_five():
    X_train, X_test, y_train, y_test = answer_four()

    knn=KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train,y_train)

    return knn
answer_five()

# 6. Using your knn classifier, predict the class label using the mean value for each feature.
# Hint: You can use cancerdf.mean()[:-1].values.reshape(1, -1) which gets the mean value for 
# each feature, ignores the target column, and reshapes the data from 1 dimension to 2 
# (necessary for the precict method of KNeighborsClassifier).

# This function should return a numpy array either array([ 0.]) or array([ 1.])
def answer_six():
    cancerdf=answer_one()
    means=cancerdf.mean()[:-1].values.reshape(1,-1)

    knn=answer_five()
    answer=knn.predict(means)

    return answer
answer_six()

# 7.Using your knn classifier, predict the class labels for the test set X_test.
# This function should return a numpy array with shape (143,) and values either 0.0 or 1.0.

def answer_seven():
    X_train, X_test, y_train, y_test = answer_four()
    knn=answer_five()  
    ansTest=knn.predict(X_test)

    return ansTest
answer_seven()

# 8 Find the score (mean accuracy) of your knn classifier using X_test and y_test.

# This function should return a float between 0 and 1

def answer_eight():
    X_train, X_test, y_train, y_test = answer_four()
    knn=answer_five()

    return meanAccuracy
answer_eight()


