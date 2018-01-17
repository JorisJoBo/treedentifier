"""
Connect the input and labels and print to file.

Call from commandline with the names of the files that are to be combined
as arguments. The first file should be the inputs and the second file
the labels.
Returns a .csv file containing the data required for machinelearning.
"""

import numpy as np
import sys

# filename1 = "combined_canopy.csv"
filename1 = sys.argv[1]
# filename2 = "dominant_trees.csv"
filename2 = sys.argv[2]

raw_metrics = np.loadtxt(open(filename1, 'rb'), dtype=str, delimiter=',')
trees = np.loadtxt(open(filename2, 'rb'), dtype=str, delimiter=';')

# sort metrics to match trees
sorted_metrics = []
for line in trees:
    polyID = line[1]
    for row in raw_metrics:
        if row[1] == polyID:
            sorted_metrics.append(row)
metrics = np.array(sorted_metrics)
X = metrics[1:]

# remove and sort trees to match sorted metrics
sorted_trees = []
for line in trees:
    if line[1] in metrics[0, :]:
        sorted_trees.append(line[:, -1])
Y = np.array(sorted_trees)

# write all relevant data to file
X = X.toList()
Y = Y.toList()
with open('learning_data.csv', 'a') as result_file:
    for line in range(len(X)):
        stringLineX = ','.join(X[line])
        stringLineY = ','.join(Y[line])
        result_file.write(stringLineX + ',' + stringLineY + '\n')
