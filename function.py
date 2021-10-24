import pandas as pd
import csv
from math import floor


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'csv'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def agecount(dataset):
    count = [0, 0, 0, 0]
    for x in range(1, len(dataset)):
        if dataset[x][-1] == 1:
            if dataset[x][0] > 75:
                count[0] += 1
            elif dataset[x][0] > 50:
                count[1] += 1
            elif dataset[x][0] > 25:
                count[2] += 1
            else:
                count[3] += 1
    return count


def gendercount(dataset):
    count = [0, 0]
    for x in range(1, len(dataset)):
        if dataset[x][-1] == 1:
            if dataset[x][1] == 1:
                count[0] += 1
            else:
                count[1] += 1
    return count


def chestpaincount(dataset):
    count = [0, 0, 0, 0]
    for x in range(1, len(dataset)):
        if dataset[x][-1] == 1:
            if dataset[x][2] == 0:
                count[0] += 1
            elif dataset[x][2] == 1:
                count[1] += 1
            elif dataset[x][2] == 2:
                count[2] += 1
            else:
                count[3] += 1
    return count


def bloodsugercount(dataset):
    count = [0, 0]
    for x in range(1, len(dataset)):
        if dataset[x][-1] == 1:
            if dataset[x][5] == 0:
                count[0] += 1
            else:
                count[1] += 1
    return count


def restegcount(dataset):
    count = [0, 0, 0]
    for x in range(1, len(dataset)):
        if dataset[x][-1] == 1:
            if dataset[x][6] == 0:
                count[0] += 1
            elif dataset[x][6] == 1:
                count[1] += 1
            else:
                count[2] += 1

    return count


def thulcount(dataset):
    count = [0, 0, 0]
    for x in range(1, len(dataset)):
        if dataset[x][-1] == 1:
            if dataset[x][12] == 1:
                count[0] += 1
            elif dataset[x][12] == 2:
                count[1] += 1
            else:
                count[2] += 1
    return count


def countpie(dataset):
    with open(dataset, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)

        for x in range(1, len(dataset)):
            for y in range(len(dataset[x])):
                dataset[x][y] = float(dataset[x][y])

        result = []
        result.append(agecount(dataset))
        result.append(gendercount(dataset))
        result.append(chestpaincount(dataset))
        result.append(bloodsugercount(dataset))
        result.append(restegcount(dataset))
        result.append(thulcount(dataset))

        return result
