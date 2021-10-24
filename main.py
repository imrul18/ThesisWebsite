from algorithm import *
from function import *

from flask import Flask, render_template, url_for, request, redirect, flash
import csv
import os

app = Flask(__name__)
app.secret_key = 'Afnan'


@app.route('/')
def index():
    dataset = 'static\data.csv'

    pie = countpie(dataset)

    clf = []

    clf.append(KNeighborsClassifier(n_neighbors=3, metric='minkowski', p=2))
    clf.append(KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2))
    clf.append(KNeighborsClassifier(n_neighbors=7, metric='minkowski', p=2))
    clf.append(DecisionTreeClassifier(random_state=0))
    clf.append(GaussianNB())
    clf.append(svm.SVC(kernel='linear'))
    clf.append(RandomForestClassifier(n_estimators=100))

    rows = []
    for i in range(0, 7):
        rows.append(analysis(clf[i], dataset))

    return render_template('dashboard.html', result=rows, pie=pie)


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
    error = ''
    result = ''
    if(request.method == 'POST'):
        if 'file' not in request.files:
            flash('No file part')
        else:
            file = request.files['file']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                error = "No file found"
            elif file and allowed_file(file.filename):

                file.save(os.path.join('file/file.csv'))
                dataset = 'file/file.csv'
                with open(dataset, 'r') as csvfile:
                    lines = csv.reader(csvfile)
                    dataset = list(lines)

                    for i in range(1, len(dataset)):
                        for j in range(len(dataset[i])-1):
                            isfloat = True
                            isint = True
                            try:
                                float(dataset[i][j])
                            except ValueError:
                                isfloat = False
                            try:
                                int(dataset[i][j])
                            except ValueError:
                                isint = False

                            if isfloat or isint:
                                isnum = 1
                            else:
                                error = "Value of attribute " + \
                                    repr(dataset[0][j]) + \
                                    " is not a Number in row number: "+repr(i)
                                isnum = 0
                                break
                        if isnum == 0:
                            break

                    if isnum == 1:

                        clf = []

                        dataset = 'file/file.csv'

                        clf.append(KNeighborsClassifier(
                            n_neighbors=3, metric='minkowski', p=2))
                        clf.append(KNeighborsClassifier(
                            n_neighbors=5, metric='minkowski', p=2))
                        clf.append(KNeighborsClassifier(
                            n_neighbors=7, metric='minkowski', p=2))
                        clf.append(DecisionTreeClassifier(random_state=0))
                        clf.append(GaussianNB())                        
                        clf.append(svm.SVC(kernel='linear'))
                        clf.append(RandomForestClassifier(n_estimators=100))

                        result = []
                        for i in range(0, 7):
                            result.append(analysis(clf[i], dataset))
            else:
                error = "Uploaded file is not in .csv format"

    return render_template('checkyourdataset.html', error=error, result=result)
