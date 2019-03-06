import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

def fillna_mean_prev_n(array, n, threshold):
    """
    Fill nan value bious n values. If value is less than threshold,
    replace it by previous one value 
    """
    for i in np.arange(0, len(array)):
        if array[i] == 0 and i >= n:
            array[i] = np.mean(array[i-n:i])
        if array[i]<threshold:
            array[i] = array[i-1]
    return array

def cat_to_num(array, threshold, converter):
    """
    Convert catagorical data (month, hour, etc) to number that appears
    to be proportional to the lable we are going to predict.
    For instance, the temp is lowest in June, and highest in December and January,
    so we lable December and January larger(positive relation) or smaller(negative relation)
    than June 
    """
    for i in np.arange(0, len(array)):
        if array[i]>threshold:
            array[i] = converter-array[i]
    return array

def to_max(df, col, adder_col, adder):
    """
    Using existing value to fill nan in columns like xmin/xmax
    For instance, using temp column to fill tmax
    """
    array = np.array(df[col])
    norm_array = np.array(df[adder_col])
    for i in np.arange(0, len(array)):
        if array[i]==0:
            array[i] = norm_array[i] + adder
    return array

def train_and_test(df, label_col, print_confidence = True):
    """
    Training LinearRegression using feature columns for label columns.
    The classifier return can then predict and fill nan values according to other
    columns.
    """
    X = np.array(df.drop([label_col], 1))
    y = np.array(df[label_col])
    X = preprocessing.scale(X)
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.1)
    clf = LinearRegression()
    clf.fit(X_train, y_train)
    if print_confidence:
        confidence = clf.score(X_test, y_test)
        print(confidence)
    return clf

def predict(df, feature_col, clf):
    """
    Fillna using predictive classifiers
    """
    predict_df = df[feature_col]
    predict_df = preprocessing.scale(predict_df)
    predicted = clf.predict(predict_df)
    return predicted

