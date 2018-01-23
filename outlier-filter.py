import csv
import sys
filename = sys.argv[1]

with open(filename) as f:
    with open('cleaned_canopy.csv', 'a') as result_file:
        f = csv.reader(f, delimiter=',')
        originalline = []
        polygonID = 0
        for line in f:
            if line[0] == 'index':
                outputline = ''
                for item in line:
                    outputline = ''
                    for item in line:
                        outputline = outputline + item + ';'
                    result_file.write(outputline[:-1] + '\n')
            else:
                if line[1] != polygonID:
                    polygonID = line[1]
                    originalline = line
                    outputline = ''
                    for item in line:
                        outputline = ''
                        for item in line:
                            outputline = outputline + item + ';'
                        result_file.write(outputline[:-1] + '\n')
                else:
                    write = True
                    for i in range(6, len(line)):
                        difference = float(line[i]) - float(originalline[i])
                        if difference**2 > (float(originalline[i]))**2:
                            write = False
                    if write == True:
                        outputline = ''
                        for item in line:
                            outputline = outputline + item + ';'
                        result_file.write(outputline[:-1] + '\n')
