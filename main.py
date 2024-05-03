# Load libraries
import sys
import scipy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


def load_data():
    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    attrs = ["sepal_length","sepal_width", "petal_length", "petal_width", "class"]
    dataset = pd.read_csv(url, names=attrs)
    dataset.columns = attrs
    return dataset

def get_separator(title = None):
    separator = "="*50
    if title:
        return "\n" + separator + " " +title+ " " + separator + "\n"
    
    return separator * 2

def show_sumary(dataset):

    print(get_separator("DATA"))
    print(dataset.head())
    print(get_separator("SHAPE"))
    print(dataset.shape)
    print(get_separator("DESCRIBE"))
    print(dataset.describe())

def main():
    dt = load_data()

    show_sumary(dt)


main()