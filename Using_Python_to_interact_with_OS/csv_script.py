import csv
"""Opening Files"""
f = open("hosts.csv")
csv_f = csv.reader(f)

for row in csv_f:
    name, phone = row
    print("Name: {}, Phone: {}".format(name, phone))
"""The Print line prints the naem and phone from each of row from the csv file"""
