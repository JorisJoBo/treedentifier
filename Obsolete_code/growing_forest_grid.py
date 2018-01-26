import csv
import sys
filename = sys.argv[1]

growing_plots = []

with open(filename) as f:
    convertedf = csv.reader(f, delimiter=';')
    # extract the coordinates from the plot string
    for line in convertedf:
        X = []
        Y = []
        # the uncertainty in meters for this line
        polyID = line[1]
        indice = line[5].find('(') + 2
        allCoords = line[5][indice:-2]
        coords = allCoords.split(',')
        for coord in coords:
            x, y = coord.split(' ')
            X.append(x)
            Y.append(y)
        size = int(max(X)) - int(min(X))
        types = [0, -size, size, -size * 2, size * 2]
        typecombinations = []
        for xtype in types:
            for ytype in types:
                typecombinations.append([xtype, ytype])

        for ux, uy in typecombinations:
            growing_plots.append([polyID,
                                  int(min(X)) + ux,
                                  int(min(Y)) + uy,
                                  int(max(X)) + ux,
                                  int(max(Y)) + uy])

# creates 9 files, for each uncertainty direction one


with open('ID_growing_forest.csv', 'a') as result_file:
    result_file.write("polygonID min_x min_y max_x max_y\n")
    for line in growing_plots:
        stringLine = ''
        for value in line:
            stringLine = stringLine + str(value)
            if value != line[-1]:
                stringLine = stringLine + ' '
        result_file.write(stringLine + '\n')
