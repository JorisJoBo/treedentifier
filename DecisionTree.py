from sklearn import tree
import csv
import numpy as np
import graphviz
import matplotlib.pylab as plt

data = []
with open('common_learning_data.csv') as f:
    f = csv.reader(f, delimiter=';')
    for line in f:
        data.append(line)

features = data[0]
data = data[1:]
removed_features = [0, 1, 2, 3, 4, 5, 19, 20, 22, 23,
                    24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
cl_features = []
cl_data = []
for i in range(len(features)):
    if i not in removed_features:
        cl_features.append(features[i])
for line in data:
    newline = []
    for i in range(len(features)):
        if i not in removed_features:
            newline.append(line[i])
    cl_data.append(newline)
features = cl_features
data = cl_data


def decisiontree(data, min_split, min_leaf, weight):
    Xt = []
    Yt = []
    Xv = []
    Yv = []
    np.random.shuffle(data)
    trainingsize = 0.8 * len(data)
    training = data[:int(trainingsize)]
    validation = data[int(trainingsize):]

    for line in training:
        Xt.append(line[0:-1])
        Yt.append(line[-1])
    clf = tree.DecisionTreeClassifier(
        min_samples_split=min_split,
        min_samples_leaf=min_leaf,
        class_weight=weight)
    clf = clf.fit(Xt, Yt)

    for line in validation:
        Xv.append(line[0:-1])
        Yv.append(line[-1])
    return clf, Xt, Yt, Xv, Yv


clf, Xt, Yt, Xv, Yv = decisiontree(data, 2, 1, None)
dot_data = tree.export_graphviz(clf, out_file=None,
                                class_names=Yt, feature_names=features[0:-1],
                                filled=True, rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('tree', view=True)

clf.score(Xv, Yv)
