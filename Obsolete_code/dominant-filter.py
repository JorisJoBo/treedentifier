import csv
import operator

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
                            rebuildline = rebuildline + ';'
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
                rebuildline = rebuildline + ';'
        result_file.write(rebuildline + '\n')
