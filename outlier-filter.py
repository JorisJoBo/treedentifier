import csv
import sys
import math
filename = sys.argv[1]

with open(filename) as f:
    with open('cleaned_canopy.csv', 'a') as result_file:
        f = csv.reader(f, delimiter=',')
        o = []
        polygonID = 0
        for line in f:
            if line[0] == 'index':
                outputline = ''
                for item in line:
                    outputline = outputline + item + ';'
                result_file.write(outputline[:-1] + '\n')
            else:
                if line[1] != polygonID:
                    polygonID = line[1]
                    o = line
                    outputline = ''
                    for item in line:
                        outputline = ''
                        for item in line:
                            outputline = outputline + item + ';'
                    result_file.write(outputline[:-1] + '\n')
                else:
                    write = True
                    for i in range(6, len(o[6:])):
                        if not abs(float(o[i]) -
                                   float(line[i])) <= max(0.75 *
                                                          abs(float(o[i])), 2):
                            write = False
                    if write:
                        outputline = ''
                        for item in line:
                            outputline = outputline + item + ';'
                        result_file.write(outputline[:-1] + '\n')
