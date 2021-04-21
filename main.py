import csv
from patient import Patient
from datetime import date

fileName = "DADSA 2021 CWK B DATA COLLECTION.csv"
patientData = []
patientsList = []
obeseMalesList = []
obeseFemalesList = []
underweightMalesList = []
underweightFemalesList = []
patientReferralList = []


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
        print("Patient Name:", i.getName(), "|| Age:", i.getAge(), "|| BMI:", i.getBMI(),
              "|| Weight Classification:",
              i.getWeightClassification())
        lineCount = lineCount + 1
        if lineCount == 10:
            print("---------------------------------------------------------------------------------")
            lineCount = 0

for i in patientsList:
    if i.getWeightClassification() == "Underweight":
        print("Patient Name:", i.getName(), "|| Age:", i.getAge(), "|| BMI:", i.getBMI(),
              "|| Weight Classification:",
              i.getWeightClassification())
        lineCount = lineCount + 1
        if lineCount == 10:
            print("---------------------------------------------------------------------------------")
            lineCount = 0

for i in patientsList:
    if i.getWeightClassification() == "Overweight":
        print("Patient Name:", i.getName(), "|| Age:", i.getAge(), "|| BMI:", i.getBMI(),
              "|| Weight Classification:",
              i.getWeightClassification())
        lineCount = lineCount + 1
        if lineCount == 10:
            print("---------------------------------------------------------------------------------")
            lineCount = 0

for i in patientsList:
    if i.getWeightClassification() == "Normal":
        print("Patient Name:", i.getName(), "|| Age:", i.getAge(), "|| BMI:", i.getBMI(),
              "|| Weight Classification:",
              i.getWeightClassification())
        lineCount = lineCount + 1
        if lineCount == 10:
            print("---------------------------------------------------------------------------------")
            lineCount = 0

for i in patientsList:
    if i.getSex() == 'M' and i.getWeightClassification() == "Obese":
        obeseMalesList.append(i)

    if i.getSex() == 'M' and i.getWeightClassification() == "Underweight":
        underweightMalesList.append(i)

    if i.getSex() == 'F' and i.getWeightClassification() == "Obese":
        obeseFemalesList.append(i)

    if i.getSex() == 'F' and i.getWeightClassification() == "Underweight":
        underweightFemalesList.append(i)

print("Worst 5 Obese Males:")
for i in obeseMalesList:
    print(i.getName())
print("----------------")

print("Worst 5 Obese Females:")
for i in obeseFemalesList:
    print(i.getName())
print("----------------")

print("Worst 5 Underweight Males:")
for i in underweightMalesList:
    print(i.getName())
print("----------------")

print("Worst 5 Underweight Females:")
for i in underweightFemalesList:
    print(i.getName())
print("----------------")

for i in patientsList:
    i.setReferralPriority()

# First priority given according to conditions specified in setReferralPriority()
for i in patientsList:
    if i.getReferralPriority() == 1:
        patientReferralList.append(i)

sortedList = []
for i in range(0, len(patientReferralList)):
    sortedList.append(patientReferralList[i])

# Bubble sort, second priority patients oldest age to youngest
for i in range(len(sortedList) - 1):
    if sortedList[i].getReferralPriority() == 2:
        if sortedList[i].getAge() < sortedList[i + 1].getAge():
            temp = sortedList[i + 1]
            sortedList[i] = sortedList[i + 1]
            sortedList[i] = temp

print("Dietitian Referrals:")
for i in patientReferralList:
    if i.getReferralPriority() == 1:
        print(i.getName())
for i in sortedList:
    print(i.getName())
