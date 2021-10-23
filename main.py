from math import floor
from algorithm import *

from flask import Flask, render_template, url_for, request, redirect, flash
import csv
import os

app = Flask(__name__)
app.secret_key = 'Afnan'


@app.route('/')
def index():
    dataset = 'static\data.csv'

    clf = []

    clf.append(KNeighborsClassifier(n_neighbors=3, metric='minkowski', p=2))
    clf.append(KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2))
    clf.append(KNeighborsClassifier(n_neighbors=7, metric='minkowski', p=2))
    clf.append(DecisionTreeClassifier(random_state=0))
    clf.append(GaussianNB())
    clf.append(RandomForestClassifier(n_estimators=100))
    clf.append(KNeighborsClassifier(n_neighbors=7, metric='minkowski', p=2))

    rows = []
    for i in range(0, 6):
        rows.append(analysis(clf[i], dataset, 'target'))

    fields = ['Name', 'Branch', 'Year', 'CGPA']

    # name of csv file
    filename = "static/analysis.csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    return render_template('dashboard.html')


@app.route('/dataset')
def dataset():
    with open('static/data.csv', 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
    return render_template('dataset.html', dataset=dataset)


@app.route('/checkyourself')
def checkyourself():
    return render_template('checkyourself.html')


@app.route('/checkyourdataset')
def checkyourdataset():
    return render_template('checkyourdataset.html', error='', result='')


@app.route('/showresult', methods=['POST'])
def showresult():
    input = [[request.form['input0'], request.form['input1'], request.form['input2'], request.form['input3'], request.form['input4'], request.form['input5'],
              request.form['input6'], request.form['input7'], request.form['input8'], request.form['input9'], request.form['input10'], request.form['input11'], request.form['input12']]]
    dataset = 'static\data.csv'

    clf = ''
    clfname = ''
    if request.form['techniques'] == '1':
        clf = KNeighborsClassifier(n_neighbors=3, metric='minkowski', p=2)
        clfname = "KNN-3"
    elif request.form['techniques'] == '2':
        clf = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
        clfname = "KNN-5"
    elif request.form['techniques'] == '3':
        clf = KNeighborsClassifier(n_neighbors=7, metric='minkowski', p=2)
        clfname = "KNN-7"
    elif request.form['techniques'] == '4':
        clf = DecisionTreeClassifier(random_state=0)
        clfname = "Decision Tree"
    elif request.form['techniques'] == '5':
        clf = GaussianNB()
        clfname = "Naive Bayes"
    elif request.form['techniques'] == '6':
        clf = svm.SVC()
        clfname = "SVM"
    else:
        clf = RandomForestClassifier(n_estimators=100)
        clfname = "Random Forest"

    result = findprediction(clf, dataset, input, clfname)

    return render_template('checkyourself.html', result=result, data=input)


@app.route('/datasetupload', methods=['POST'])
def showdatasetresult():
    if(request.method == 'POST'):
        file = request.files['upforcheck']
        file.save(os.path.join('file/file.csv'))

    dataset = 'file/file.csv'

    clf = []

    clf.append(KNeighborsClassifier(n_neighbors=3, metric='minkowski', p=2))
    clf.append(KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2))
    clf.append(KNeighborsClassifier(n_neighbors=7, metric='minkowski', p=2))
    clf.append(DecisionTreeClassifier(random_state=0))
    clf.append(GaussianNB())
    clf.append(RandomForestClassifier(n_estimators=100))
    clf.append(KNeighborsClassifier(n_neighbors=7, metric='minkowski', p=2))

    result = []
    for i in range(0, 7):
        result.append(analysis(clf[i], dataset, 'Drug'))

    return render_template('checkyourdataset.html', error='', result=result)
