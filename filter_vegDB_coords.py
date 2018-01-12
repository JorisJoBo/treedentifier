# load data:
trees = np.loadtxt(open(datafile, 'rb'), dtype=str, delimiter=';')

# filter out the plot id and coordinates
raw_polys = []
polys = []
for line in trees:
    raw_polys.append([line[1], line[5]])
for line in raw_polys:
    if line not in polys:
        polys.append(l)

# extract the coordinates from the plot string
plots = []
for line in polys:
    X = []
    Y = []
    polyID = l[0]
    allCoords = l[1][9:-2]
    coords = allCoords.split(',')
    for coord in coords:
        x, y = c.split(' ')
        X.append(x)
        Y.append(y)
    plots.append([polyID, min(X), min(Y), max(X), max(Y)])

# write coordinates to file with corrosponding polygonID
with open('ID_forest_grid_coords.csv', 'a') as result_file:
    result_file.write("polygonID min_x min_y max_x max_y\n")
    for line in plots:
        stringLine = ' '.join(line)
        result_file.write(stringLine+'\n')

# write coordinates to file in LAStools interpretable style
with open('forest_grid_coords.csv', 'a') as result_file:
    for line in plots:
        stringLine = ' '.join(line[1:])
        result_file.write(stringLine+'\n')
