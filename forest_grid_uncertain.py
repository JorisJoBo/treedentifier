import csv
import sys
filename = sys.argv[1]

plots_n = []
plots_e = []
plots_s = []
plots_w = []
plots_nw = []
plots_ne = []
plots_sw = []
plots_se = []

with open(filename) as f:
    convertedf = csv.reader(f, delimiter=';')
    for line in convertedf:
        X = []
        Y = []
        u = int(line[4])
        polyID = line[1]
        indice = line[5].find('(') + 2
        allCoords = line[5][indice:-2]
        coords = allCoords.split(',')
        for coord in coords:
            x, y = coord.split(' ')
            X.append(x)
            Y.append(y)
        plots_n.append([polyID, int(min(X)), int(min(Y)) +
                        u, int(min(X)), int(min(Y)) + u])
        plots_e.append([polyID, int(min(X)) + u, int(min(Y)),
                        int(min(X)) + u, int(min(Y))])
        plots_s.append([polyID, int(min(X)), int(min(Y)) -
                        u, int(min(X)), int(min(Y)) - u])
        plots_w.append([polyID, int(min(X)) - u, int(min(Y)),
                        int(min(X)) - u, int(min(Y))])
        plots_nw.append([polyID,
                         int(min(X)) - u,
                         int(min(Y)) + u,
                         int(min(X)) - u,
                         int(min(Y)) + u])
        plots_ne.append([polyID,
                         int(min(X)) + u,
                         int(min(Y)) + u,
                         int(min(X)) + u,
                         int(min(Y)) + u])
        plots_sw.append([polyID,
                         int(min(X)) - u,
                         int(min(Y)) - u,
                         int(min(X)) - u,
                         int(min(Y)) - u])
        plots_se.append([polyID,
                         int(min(X)) + u,
                         int(min(Y)) - u,
                         int(min(X)) + u,
                         int(min(Y)) - u])

with open('ID_uncertain_forest_north.csv', 'a') as result_file:
    result_file.write("polygonID min_x min_y max_x max_y\n")
    for line in plots_n:
        stringLine = ''
        for value in line:
            stringLine = stringLine + str(value)
            if value != line[-1]:
                stringLine = stringLine + ' '
        result_file.write(stringLine + '\n')

with open('ID_uncertain_forest_east.csv', 'a') as result_file:
    result_file.write("polygonID min_x min_y max_x max_y\n")
    for line in plots_e:
        stringLine = ''
        for value in line:
            stringLine = stringLine + str(value)
            if value != line[-1]:
                stringLine = stringLine + ' '
        result_file.write(stringLine + '\n')

with open('ID_uncertain_forest_south.csv', 'a') as result_file:
    result_file.write("polygonID min_x min_y max_x max_y\n")
    for line in plots_s:
        stringLine = ''
        for value in line:
            stringLine = stringLine + str(value)
            if value != line[-1]:
                stringLine = stringLine + ' '
        result_file.write(stringLine + '\n')

with open('ID_uncertain_forest_west.csv', 'a') as result_file:
    result_file.write("polygonID min_x min_y max_x max_y\n")
    for line in plots_w:
        stringLine = ''
        for value in line:
            stringLine = stringLine + str(value)
            if value != line[-1]:
                stringLine = stringLine + ' '
        result_file.write(stringLine + '\n')

with open('ID_uncertain_forest_northwest.csv', 'a') as result_file:
    result_file.write("polygonID min_x min_y max_x max_y\n")
    for line in plots_nw:
        stringLine = ''
        for value in line:
            stringLine = stringLine + str(value)
            if value != line[-1]:
                stringLine = stringLine + ' '
        result_file.write(stringLine + '\n')

with open('ID_uncertain_forest_northeast.csv', 'a') as result_file:
    result_file.write("polygonID min_x min_y max_x max_y\n")
    for line in plots_ne:
        stringLine = ''
        for value in line:
            stringLine = stringLine + str(value)
            if value != line[-1]:
                stringLine = stringLine + ' '
        result_file.write(stringLine + '\n')

with open('ID_uncertain_forest_southwest.csv', 'a') as result_file:
    result_file.write("polygonID min_x min_y max_x max_y\n")
    for line in plots_sw:
        stringLine = ''
        for value in line:
            stringLine = stringLine + str(value)
            if value != line[-1]:
                stringLine = stringLine + ' '
        result_file.write(stringLine + '\n')

with open('ID_uncertain_forest_southeast.csv', 'a') as result_file:
    result_file.write("polygonID min_x min_y max_x max_y\n")
    for line in plots_se:
        stringLine = ''
        for value in line:
            stringLine = stringLine + str(value)
            if value != line[-1]:
                stringLine = stringLine + ' '
        result_file.write(stringLine + '\n')
