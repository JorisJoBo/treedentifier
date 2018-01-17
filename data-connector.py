"""
Connect the input and labels and print to file.

Call from commandline with the names of the files that are to be combined
as arguments. The first file should be the inputs and the second file
the labels.
Returns a .csv file containing the data required for machinelearning.
"""

import sys
import csv

# filename1 = "combined_canopy.csv"
filename1 = sys.argv[1]
# filename2 = "dominant_trees.csv"
filename2 = sys.argv[2]

with open(filename1) as f1:
    with open(filename2) as f2:
        with open('learning_data.csv', 'a') as result_file:
            f1 = csv.reader(f1, delimiter=',')
            f2 = csv.reader(f2, delimiter=';')
            latindict = {}
            for line in f2:
                latindict[line[1]] = line[7]
            next(f1)
            for line in f1:
                latinname = latindict[line[1]]
                line.append(latinname)
                outputline = ''
                for item in line:
                    outputline = outputline + item
                    if item != line[-1]:
                        outputline = outputline + ';'
                result_file.write(outputline + '\n')
