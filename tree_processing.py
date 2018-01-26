import csv
import operator

treespecies = []
with open('treespecies.txt') as b:
    for species in b:
        treespecies.append(species)

with open('joined_db2.csv') as f:
    with open('forest_filter_result.csv', 'a') as result_file:
        for line in f:
            if 'Forest' in line:
                for species in treespecies:
                    if species in line:
                        result_file.write(line)

with open('forest_filter_result.csv') as f:
    with open('dominant_trees.csv', 'a') as result_file:
        convertedf = csv.reader(f, delimiter=';')
        # groups all lines in the csv file on polygonID
        sortedf = sorted(convertedf, key=operator.itemgetter(1))
        current_polygon = ''
        dominant_tree = ''
        dominant_tree_ratio = 0
        for line in sortedf:
            # if a new polygonID is found, write the dominant tree of the
            # previous polygonID to the resultfile
            if line[1] != current_polygon:
                if current_polygon != '':
                    for data in dominant_tree:
                        rebuildline = rebuildline + data
                        if data != dominant_tree[-1]:
                            rebuildline = rebuildline + ','
                    result_file.write(rebuildline + '\n')
                current_polygon = line[1]
                dominant_tree_ratio = 0
                rebuildline = ''
            # if current quantity percentage is higher than highest
            # percentage for this polygonID, replace the old one
            if float(line[3]) > float(dominant_tree_ratio):
                dominant_tree = line
                dominant_tree_ratio = line[3]
        # adds the last dominant_tree to the result file
        for data in dominant_tree:
            rebuildline = rebuildline + data
            if data != dominant_tree[-1]:
                rebuildline = rebuildline + ','
        result_file.write(rebuildline + '\n')

growing_plots = []

with open('dominant_trees.csv') as f:
    convertedf = csv.reader(f, delimiter=',')
    # extract the coordinates from the plot string
    for line in convertedf:
        X = []
        Y = []

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

with open('ID_growing_forest.csv', 'a') as result_file:
    result_file.write("polygonID min_x min_y max_x max_y\n")
    for line in growing_plots:
        stringLine = ''
        for value in line:
            stringLine = stringLine + str(value)
            if value != line[-1]:
                stringLine = stringLine + ' '
        result_file.write(stringLine + '\n')
