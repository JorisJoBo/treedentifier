import csv

with open("common_learning_data.csv") as f:
    with open("relative_learning_data.csv", 'w') as result_file:
        f = csv.reader(f, delimiter=";")
        data = []
        for line in f:
            data.append(line)
        result_file.write(','.join(data[0]) + '\n')
        for line in data[1:]:
            newline = ''
            count = 0
            locations = [13, 14, 15, 16, 17, 18]
            for element in line:
                if count in locations:
                    newline = newline + \
                        str(float(element) / float(line[7])) + ','
                else:
                    newline = newline + str(element) + ','
                count += 1
            result_file.write(newline[:-1] + '\n')
