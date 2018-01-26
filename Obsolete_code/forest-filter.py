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
