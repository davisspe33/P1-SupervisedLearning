
import csv
import numpy as np 
import pandas as pd 
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import validation_curve
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve

def main():
    x, y = transformData()
    #svr_poly_kernal(x,y)
    # plotmodel(x,y)
    # plotmodelC(x,y)
    #plotmodelep(x,y)
    #plotmodelLearn(x,y)

def transformData(): 
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

def plotmodelLearn(x,y):
    _, axes = plt.subplots(1, 2, figsize=(20, 5))
    axes[0].set_xlabel("Training examples")
    axes[0].set_ylabel("Score")

    train_sizes=np.linspace(.1, 1.0, 5)
    train_sizes, train_scores, test_scores, fit_times, _ = learning_curve(SVR(kernel='linear'), x, y, train_sizes=train_sizes, return_times=True)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    fit_times_mean = np.mean(fit_times, axis=1)
    fit_times_std = np.std(fit_times, axis=1)
    # Plot learning curve
    axes[0].grid()
    axes[0].fill_between(train_sizes, train_scores_mean - train_scores_std,
                         train_scores_mean + train_scores_std, alpha=0.1,
                         color="r")
    axes[0].fill_between(train_sizes, test_scores_mean - test_scores_std,
                         test_scores_mean + test_scores_std, alpha=0.1,
                         color="g")
    axes[0].plot(train_sizes, train_scores_mean, 'o-', color="r",
                 label="Training score")
    axes[0].plot(train_sizes, test_scores_mean, 'o-', color="g",
                 label="Cross-validation score")
    axes[0].legend(loc="best")
    axes[0].set_title("Learning Curve")
    # Plot n_samples vs fit_times
    axes[1].grid()
    axes[1].plot(train_sizes, fit_times_mean, 'o-')
    axes[1].fill_between(train_sizes, fit_times_mean - fit_times_std,
                         fit_times_mean + fit_times_std, alpha=0.1)
    axes[1].set_xlabel("Training examples")
    axes[1].set_ylabel("fit_times")
    axes[1].set_title("Scalability of the model")
    plt.show()

main()
