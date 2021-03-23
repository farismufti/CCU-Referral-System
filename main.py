import csv
from patient import Patient
from datetime import date

fileName = "DADSA 2021 CWK B DATA COLLECTION.csv"
patientData = []
patientsList = []


def calculateAge(date):
    today = date.today()
    return today.year - date.year - ((today.month, today.day) < (date.month, date.day))


with open(fileName, 'r') as data:
    reader = csv.reader(data)
    next(reader)

    for row in reader:
        dob = row[1]
        splitString = dob.split("/")
        patientAge = calculateAge(date(int(splitString[2]), int(splitString[1]), int(splitString[0])))

        p = Patient(row[0], int(patientAge), row[2], float(row[3]), int(row[4]), row[5], row[6], row[7], row[8], row[9],
                    row[10], row[11], row[12])
        patientsList.append(p)

lineCount = 0
for i in patientsList:
    if i.getWeightClassification() == "Obese":
        print("Patient Name:", i.getName(), "|| Age:", i.getAge(), "|| BMI:", i.getBMI(), "|| Weight Classification:",
              i.getWeightClassification())
        lineCount = lineCount + 1
        if lineCount == 10:
            print("---------------------------------------------------------------------------------")
            lineCount = 0


for i in patientsList:
    if i.getWeightClassification() == "Underweight":
        print("Patient Name:", i.getName(), "|| Age:", i.getAge(), "|| BMI:", i.getBMI(), "|| Weight Classification:",
              i.getWeightClassification())
        lineCount = lineCount + 1
        if lineCount == 10:
            print("---------------------------------------------------------------------------------")
            lineCount = 0


for i in patientsList:
    if i.getWeightClassification() == "Overweight":
        print("Patient Name:", i.getName(), "|| Age:", i.getAge(), "|| BMI:", i.getBMI(), "|| Weight Classification:",
              i.getWeightClassification())
        lineCount = lineCount + 1
        if lineCount == 10:
            print("---------------------------------------------------------------------------------")
            lineCount = 0


for i in patientsList:
    if i.getWeightClassification() == "Normal":
        print("Patient Name:", i.getName(), "|| Age:", i.getAge(), "|| BMI:", i.getBMI(), "|| Weight Classification:",
              i.getWeightClassification())
        lineCount = lineCount + 1
        if lineCount == 10:
            print("---------------------------------------------------------------------------------")
            lineCount = 0
