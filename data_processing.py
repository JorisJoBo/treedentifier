'''
 add_canopy_files.py

 usage for map: add_canopy_files.py input_directory output.csv
 usage for single file: add_canopy_files.py input.csv output.csv

 Adds together all csv files generated from lascanopy and removes lines
 with missing values. Can also be used to remove lines with missing values
 from a single csv file.
 The map containing the csv files that have to be combined has to be
 present in the same directory as this file.
 Further uses dominant_trees.csv to create data suitable for learning
 algorithms.
'''
import os
from sys import argv
import sys
import csv

dirname = argv[1]
try:
    outputfile = argv[2]
except BaseException:
    print("no output file given, output saved to 'combined_canopy.csv'")
    outputfile = "combined_canopy.csv"

lines = []
header = None
if dirname.endswith('.csv'):
    with open(dirname, 'r') as f:
        for i, line in enumerate(f, 0):
            if i != 0:
                lines.append(line)
            else:
                header = line
else:
    for file in os.listdir(dirname):
        if file.endswith(".csv"):
            with open(dirname + '/' + file, 'r') as f:
                for i, line in enumerate(f, 0):
                    if i != 0:
                        lines.append(line)
                    else:
                        header = line

with open(outputfile, 'w') as f:
    f.write(header)
    for line in lines:
        line2 = line.split(',')
        if "-" not in line2:
            f.write(line)

with open(outputfile) as f:
    with open('cleaned_canopy.csv', 'a') as result_file:
        f = csv.reader(f, delimiter=',')
        o = []
        polygonID = 0
        for line in f:
            if line[0] == 'index':
                outputline = ''
                for item in line:
                    outputline = outputline + item + ','
                result_file.write(outputline[:-1] + '\n')
            else:
                if line[1] != polygonID:
                    polygonID = line[1]
                    o = line
                    outputline = ''
                    for item in line:
                        outputline = ''
                        for item in line:
                            outputline = outputline + item + ','
                    result_file.write(outputline[:-1] + '\n')
                else:
                    write = True
                    for i in range(6, len(o[6:])):
                        if not abs(float(o[i]) -
                                   float(line[i])) <= max(0.2 *
                                                          abs(float(o[i])), 2):
                            write = False
                    if write:
                        outputline = ''
                        for item in line:
                            outputline = outputline + item + ','

                        result_file.write(outputline[:-1] + '\n')

with open('cleaned_canopy.csv') as f1:
    with open('dominant_trees.csv') as f2:
        with open('learning_data.csv', 'a') as result_file:
            f1 = csv.reader(f1, delimiter=',')
            f2 = csv.reader(f2, delimiter=',')
            latindict = {}
            # uses dominant_trees to find the name, and put it in a dictionary
            for line in f2:
                latindict[line[1]] = line[-1]
            # use the dictionary to find the treename and add it to the line
            for line in f1:
                if line[0] == 'index':
                    line.append('latinname')
                else:
                    latinname = latindict[line[1]]
                    line.append(latinname)
                outputline = ''
                for item in line:
                    outputline = outputline + item
                    if item != line[-1]:
                        outputline = outputline + ','
                result_file.write(outputline + '\n')

lis = []

with open('learning_data.csv', 'r') as f:
    for i, line in enumerate(f, 0):
        if i > 0:
            species = line.split(',')[-1].rstrip('\n')

            if species not in lis:
                lis.append(species)

with open('indexed_learning_data.csv', 'w') as f2:
    with open('learning_data.csv', 'r') as f:
        for line in f:
            species = line.split(',')[-1].rstrip('\n')
            if species in lis:
                write_str = line.rstrip('\n') + ',' + \
                    str(lis.index(species)) + '\n'
            else:
                write_str = line.rstrip('\n') + ', species_index' + '\n'
            f2.write(write_str)

with open("learning_data.csv") as f1:
    with open("common_learning_data.csv", 'w') as f2:
        lines = csv.reader(f1, delimiter=",")
        data = []
        for line in lines:
            data.append(line)
        seen = []
        for line1 in data:
            if line1 == data[0]:
                f2.write(','.join(line1) + '\n')
            c = line1[-1]
            if c not in seen:
                counter = 0
                for line2 in data:
                    if line2[-1] == c:
                        counter += 1
                if counter >= 50:
                    seen.append(c)
                    f2.write(','.join(line1) + '\n')
            else:
                f2.write(','.join(line1) + '\n')

with open("common_learning_data.csv") as f:
    with open("relative_learning_data.csv", 'w') as result_file:
        f = csv.reader(f, delimiter=",")
        data = []
        for line in f:
            data.append(line)
        result_file.write(','.join(data[0]) + '\n')
        for line in data[1:]:
            newline = ''
            count = 0
            locations = [13, 14, 15, 16, 17, 18]
            for element in line:
                if count in locations:
                    newline = newline + \
                        str(float(element) / float(line[7])) + ','
                else:
                    newline = newline + str(element) + ','
                count += 1
            result_file.write(newline[:-1] + '\n')
