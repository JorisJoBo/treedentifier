#  Filter the Forest

with open('joined_db2.csv') as f:
    with open('forest_filter_result.csv', 'a') as result_file:
        for line in f:
            if 'Forest' in line:
                result_file.write(line)
