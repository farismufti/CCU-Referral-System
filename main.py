import csv

fileName = "DADSA 2021 CWK B DATA COLLECTION.csv"
patientData = []

with open(fileName, 'r') as data:
    reader = csv.reader(data)
    next(reader)

    for row in reader:
        patientData = row

