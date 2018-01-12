#  Filter the Forest

with open('joined_db2.csv') as f:
    forestEntries = []
    for line in f:
        if 'Forest' in line:
            forestEntries.append(line)

    with open('forest_filter_result.csv', 'a') as result_file:
        for entry in forestEntries:
            result_file.write(entry)
