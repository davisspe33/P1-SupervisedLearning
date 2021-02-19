
import csv
import numpy as np 
import pandas as pd 
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import validation_curve
import matplotlib.pyplot as plt

def main():
    x, y = transformCreditData()
    #svr_poly_kernal(x,y)
    # plotmodel(x,y)
    # plotmodelC(x,y)
    plotmodelep(x,y)

def transformCreditData(): 
    data = pd.read_csv('HousingData.csv') 
    data = data.fillna(0)
    x = data
    x = x.drop(['MEDV'], axis=1)
    y = data['MEDV']
    return x,y

def svr_poly_kernal(x,y):
    clf = make_pipeline(StandardScaler(), SVR(kernel='linear'))
    scores = cross_val_score(clf, x, y, cv=5, verbose=1)
    print(scores)

def plotmodel(x,y):
    param_range= np.linspace(1, 10, num=10)
    param_range= param_range.astype('int')
    train_scores, test_scores = validation_curve(SVR(kernel='poly'), x, y, param_name="degree", param_range=param_range, cv=5)
    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    lw = 2
    plt.plot(param_range, train_scores_mean, label="Training score",color="darkorange", lw=lw)
    plt.plot(param_range, test_scores_mean, label="Cross-validation score",color="navy", lw=lw)
    plt.xlabel('degree')
    plt.ylabel('R squared accuracy')
    plt.legend(loc="best")
    plt.show()

def plotmodelC(x,y):
    param_range= np.linspace(1.1, 0.2, num=3)
    print(param_range)
    train_scores, test_scores = validation_curve(SVR(kernel='linear'), x, y, param_name="C", param_range=param_range, cv=5)
    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    lw = 2
    plt.plot(param_range, train_scores_mean, label="Training score",color="darkorange", lw=lw)
    plt.plot(param_range, test_scores_mean, label="Cross-validation score",color="navy", lw=lw)
    plt.xlabel('C: Regularization parameter')
    plt.ylabel('R squared accuracy')
    plt.legend(loc="best")
    plt.show()
def plotmodelep(x,y):
    param_range= np.linspace(.05, 0.2, num=5)
    print(param_range)
    train_scores, test_scores = validation_curve(SVR(kernel='linear'), x, y, param_name="epsilon", param_range=param_range, cv=5)
    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    lw = 2
    plt.plot(param_range, train_scores_mean, label="Training score",color="darkorange", lw=lw)
    plt.plot(param_range, test_scores_mean, label="Cross-validation score",color="navy", lw=lw)
    plt.xlabel('epsilon')
    plt.ylabel('R squared accuracy')
    plt.legend(loc="best")
    plt.show()
main()
