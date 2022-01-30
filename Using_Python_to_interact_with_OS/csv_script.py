import csv

f = open("csv_file.txt")
csv_f = csv.reader(f)

for row in csv_f:
    name, phone = f
    print("Name: {}, Phone: {}".format(name, phone))

