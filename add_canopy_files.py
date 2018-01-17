'''
 add_canopy_files.py

 adds together all csv files generated from lascanopy
 the directory with csv files that have to be combined has to be
 present in the same directory as this file.
'''
import os

dirname = "canopyfiles"
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
        f.write(line)
