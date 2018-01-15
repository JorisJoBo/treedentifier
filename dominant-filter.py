import csv
import operator

with open('forest_filter_result.csv') as f:
    with open('dominant_trees.csv', 'a') as result_file:
        convertedf = csv.reader(f, delimiter=';')
        sortedf = sorted(convertedf, key=operator.itemgetter(5), reverse=True)
        current_polygon = ''
        dominant_tree = ''
        dominant_tree_ratio = 0
        for line in sortedf:
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
            if float(line[3]) > float(dominant_tree_ratio):
                dominant_tree = line
                dominant_tree_ratio = line[3]
        for data in dominant_tree:
            rebuildline = rebuildline + data
            if data != dominant_tree[-1]:
                rebuildline = rebuildline + ';'
        result_file.write(rebuildline + '\n')
