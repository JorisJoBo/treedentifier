'''
 add_canopy_files.py

 usage: add_canopy_files.py input_directory output.csv

 Adds together all csv files generated from lascanopy.
 The map containing the csv files that have to be combined has to be
 present in the same directory as this file.
'''
import os
from sys import argv

dirname = argv[1]
try:
    outputfile = argv[2]
except BaseException:
    print("no output file given, output saved to 'combined_canopy.csv'")
    outputfile = "combined_canopy.csv"

lines = []
header = None
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
        if "-" not in line:
            f.write(line)
