from sklearn import tree
import csv
import numpy as np
import graphviz
import matplotlib.pylab as plt

# Converts relative_learning_data.csv to a list
data = []
with open('relative_learning_data.csv') as f:
    f = csv.reader(f, delimiter=',')
    for line in f:
        data.append(line)

features = data[0]
classes = []
data = data[1:]
# ID's of columns that aren't usefull for decision trees.
removed_features = [0, 1, 2, 3, 4, 5]

# Removes these columns from the feature names and the dataset.
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


def decisiontree(data):
    Xt = []
    Yt = []
    Xv = []
    Yv = []
    # Adds 90% of the data to the trainingsset, 10% to the validationset.
    np.random.shuffle(data)
    trainingsize = 0.9 * len(data)
    training = data[:int(trainingsize)]
    validation = data[int(trainingsize):]

    # Creates the X and Y parts of the training and test sets.
    # Also fills the tree species list (classes) with all different species.
    for line in training:
        if line[-1] not in classes:
            classes.append(line[-1])
        Xt.append(line[0:-1])
        Yt.append(line[-1])
    for line in validation:
        if line[-1] not in classes:
            return decisiontree(data)
        Xv.append(line[0:-1])
        Yv.append(line[-1])

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(Xt, Yt)
    return clf, Xt, Yt, Xv, Yv


clf, Xt, Yt, Xv, Yv = decisiontree(data)
# Sorts the classes alphabetically, which makes them work as class_names
classes.sort()

# This creates an image of the decisiontree and exports it as a PDF.
dot_data = tree.export_graphviz(clf,
                                out_file=None,
                                class_names=classes,
                                feature_names=features[:-1],
                                rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('tree', view=True)


# This calculates the average correctness for the dataset.
def avgcost(data, n):
    totalcost = 0
    for i in range(n):
        clf, Xt, Yt, Xv, Yv = decisiontree(data)
        totalcost = totalcost + clf.score(Xv, Yv)
    return totalcost / n


print('Average Correctness: ' + str(avgcost(data, 500)))


# This calculates the usage (/importance) for all features in the decisiontree.
def avgimportance(data, n, features):
    totalimportance = []
    for i in range(n):
        clf, _, _, _, _ = decisiontree(data)
        importance = clf.feature_importances_
        if len(totalimportance) == 0:
            totalimportance = importance
        else:
            totalimportance = [
                x + y for x,
                y in zip(
                    totalimportance,
                    importance)]
    for i in range(len(importance)):
        print(str(features[i]) + ': ' + str(totalimportance[i] / n))


avgimportance(data, 500, features)
