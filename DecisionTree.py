from sklearn import tree
import csv
import numpy as np
import graphviz

data = []
with open('learning_data.csv') as f:
    f = csv.reader(f, delimiter=';')
    for line in f:
        data.append(line)

features = data[0]
data = data[1:]
np.random.shuffle(data)
trainingsize = 0.9 * len(data)
training = data[:int(trainingsize)]
validation = data[int(trainingsize):]

Xt = []
Yt = []
for line in training:
    Xt.append(line[7:-2])
    Yt.append(line[-1])
clf = tree.DecisionTreeClassifier()
# min_samples_split, min_samples_leaf
clf = clf.fit(Xt, Yt)

Xv = []
Yv = []
for line in validation:
    Xv.append(line[7:-2])
    Yv.append(line[-1])

dot_data = tree.export_graphviz(clf, out_file=None,
                                class_names=Yt, feature_names=features[7:-2],
                                filled=True, rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('tree', view=True)

clf.score(Xv, Yv)
