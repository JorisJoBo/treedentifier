import csv
import operator

dominant_tree_ids = []
with open('forest_filter_result.csv') as f:
        convertedf = csv.reader(f, delimiter=';')
        sortedf = sorted(convertedf, key=operator.itemgetter(5), reverse=True)
        current_polygon = ''
        dominant_tree = ''
        dominant_tree_ratio = 0
        linecount = 0
        for line in sortedf:
            if line[5] != current_polygon:
                current_polygon = line[5]
                dominant_tree_ratio = 0
                dominant_tree_ids.append(linecount)
            if float(line[3]) > float(dominant_tree_ratio):
                dominant_tree = linecount
                dominant_tree_ratio = line[3]
            linecount += 1

with open('forest_filter_result.csv') as f:
    with open('dominant_trees.csv', 'a') as result_file:
        linecount = 0
        for line in f:
            if linecount in dominant_tree_ids:
                result_file.write(line)
            linecount += 1
