
import csv
import numpy as np 
import pandas as pd 
from sklearn.model_selection import cross_val_score
from sklearn import tree
from sklearn.model_selection import validation_curve
import matplotlib.pyplot as plt

def main():
    x, y = transformCreditData()
    decisionTreeRegressor(x,y)
    plotmodel(x,y)
def transformCreditData(): 
    data = pd.read_csv('HousingData.csv') 
    data = data.fillna(0)
    x = data
    x = x.drop(['MEDV'], axis=1)
    y = data['MEDV']
    return x,y

def decisionTreeRegressor(x,y):
    clf = tree.DecisionTreeRegressor(random_state=0, max_depth=10)
    scores = cross_val_score(clf, x, y, cv=5)
    print(scores)

def plotmodel(x,y):
    param_range= np.linspace(1, 10)
    train_scores, test_scores = validation_curve(tree.DecisionTreeRegressor(random_state=0), x, y, param_name="max_depth", param_range=param_range, cv=5)
    print(train_scores)
    print(test_scores)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    lw = 2
    plt.semilogx(param_range, train_scores_mean, label="Training score",
             color="darkorange", lw=lw)
    plt.fill_between(param_range, train_scores_mean - train_scores_std,
                    train_scores_mean + train_scores_std, alpha=0.2,
                    color="darkorange", lw=lw)
    plt.semilogx(param_range, test_scores_mean, label="Cross-validation score",
                color="navy", lw=lw)
    plt.fill_between(param_range, test_scores_mean - test_scores_std,
                    test_scores_mean + test_scores_std, alpha=0.2,
                    color="navy", lw=lw)
    plt.legend(loc="best")
    plt.show()
main()
