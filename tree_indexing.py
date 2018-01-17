'''
tree_indexing.py

usage: tree_indexing inputfile.csv outputfile.csv

indexes tree species by giving each species an unique number
'''
import sys

# load data:
filename = sys.argv[1]
output_file = sys.argv[2]

list = []

with open(filename, 'r') as f:
    for i, line in enumerate(f,0):
        if i >0:
            species = line.split(';')[-1].rstrip('\n')

            if species not in list:
                list.append(species)
f.close()

with open(output_file, 'w') as f2:
    with open(filename, 'r') as f:
        for line in f:
            species = line.split(';')[-1].rstrip('\n')
            if species in list:
                write_str = line.rstrip('\n') + ';' +str(list.index(species)) + '\n'
            else:
                write_str = line.rstrip('\n') + '; species_index' + '\n'
            f2.write(write_str)
