from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import pandas as pd
from sklearn.model_selection import train_test_split
import csv
from math import floor


def findprediction(clf, dname, inputdata, clfname):
    data = pd.read_csv(dname)
    data.head()
    x_train, x_test, y_train, y_test = train_test_split(
        data, data.pop('target'), test_size=0.30, random_state=5)
    clf.fit(x_train, y_train)
    predict = clf.predict(inputdata)

    if predict[0] == 1:
        return [0, "Sorry to say", repr(clfname)+" says, Your Heart Disease prediction is Positive!!!"]
    elif predict[0] == 0:
        return [1, "Congratulation, Lucky man", repr(clfname)+" says, Your Heart Disease prediction is Negative!!!"]
    else:
        return [0, "Server Maintainance Problem", "Try Again Later!"]


def findaccuracy(clf, dname, target):
    data = pd.read_csv(dname)
    data.head()
    x_train, x_test, y_train, y_test = train_test_split(
        data, data.pop(target), test_size=0.30, random_state=5)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    return (floor(accuracy*10000)/100)


def findprecision(clf, dname, target):
    data = pd.read_csv(dname)
    data.head()
    x_train, x_test, y_train, y_test = train_test_split(
        data, data.pop(target), test_size=0.30, random_state=5)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    precision = metrics.precision_score(y_test, y_pred, average='macro')
    return (floor(precision*10000)/100)


def findrecall(clf, dname, target):
    data = pd.read_csv(dname)
    data.head()
    x_train, x_test, y_train, y_test = train_test_split(
        data, data.pop(target), test_size=0.30, random_state=5)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    recall = metrics.recall_score(y_test, y_pred, average='macro')
    return (floor(recall*10000)/100)


def findf1measure(clf, dname, target):
    data = pd.read_csv(dname)
    data.head()
    x_train, x_test, y_train, y_test = train_test_split(
        data, data.pop(target), test_size=0.30, random_state=5)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    f1measure = metrics.f1_score(y_test, y_pred, average='macro')
    return (floor(f1measure*10000)/100)


def analysis(clf, dname):
    result = []
    with open(dname, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)

        target = dataset[0][-1]

    result.append(findaccuracy(clf, dname, target))
    result.append(findprecision(clf, dname, target))
    result.append(findrecall(clf, dname, target))
    result.append(findf1measure(clf, dname, target))
    return result
