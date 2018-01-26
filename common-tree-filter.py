import csv

with open("learning_data.csv") as f1:
    with open("common_learning_data.csv", 'w') as f2:
        lines = csv.reader(f1, delimiter=";")
        data = []
        for line in lines:
            data.append(line)
        seen = []
        for line1 in data:
            if line1 == data[0]:
                f2.write(';'.join(line1) + '\n')
            c = line1[-1]
            if c not in seen:
                counter = 0
                for line2 in data:
                    if line2[-1] == c:
                        counter += 1
                if counter >= 50:
                    seen.append(c)
                    f2.write(';'.join(line1) + '\n')
            else:
                f2.write(';'.join(line1) + '\n')
