from main import patientsList, patientReferralList


class Patient:
    def __init__(self, name, age, sex, height, weight, bodyBuild, isSmoker, isAsthmatic, isIntubated, hasHypertension,
                 didRenalRT, didIntestinalSurgery, needsParenteralNutrition):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.bodyBuild = bodyBuild
        self.isSmoker = isSmoker
        self.isAsthmatic = isAsthmatic
        self.isIntubated = isIntubated
        self.hasHypertension = hasHypertension
        self.didRenalRT = didRenalRT
        self.didIntestinalSurgery = didIntestinalSurgery
        self.needsParenteralNutrition = needsParenteralNutrition
        self.BMI = self.getWeight() / (self.getHeight() ** 2)
        self.referralPriority = 0
        self.numOfConditions = 0

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setSex(self, sex):
        self.sex = sex

    def setHeight(self, height):
        self.height = height

    def setWeight(self, weight):
        self.weight = weight

    def setBodyBuild(self, bodyBuild):
        self.bodyBuild = bodyBuild

    def isSmoker(self):
        x = False
        if self.isSmoker != '':
            x = True
        return x

    def isAsthmatic(self):
        x = False
        if self.isAsthmatic != '':
            x = True
        return x

    def isIntubated(self):
        x = False
        if self.isIntubated != '':
            x = True
        return x

    def hasHypertension(self):
        x = False
        if self.hasHypertension != '':
            x = True
        return x

    def didRenalRT(self):
        x = False
        if self.didRenalRT != '':
            x = True
        return x

    def didIntestinalSurgery(self):
        x = False
        if self.didIntestinalSurgery != '':
            x = True
        return x

    def needsParenteralNutrition(self):
        x = False
        if self.needsParenteralNutrition != '':
            x = True
        return x

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getSex(self):
        return self.sex

    def getHeight(self):
        return self.height

    def getWeight(self):
        return self.weight

    def getBodyBuild(self):
        return self.bodyBuild

    def getBMI(self):
        return round(float(self.BMI), 1)

    def getWeightClassification(self):
        if self.getBMI() < 18.5:
            weightClassification = "Underweight"

        elif 18.5 <= self.getBMI() < 25.0:
            weightClassification = "Normal"

        elif self.getBodyBuild() == "Slim" and (self.getBMI() >= 25.0 or self.getBMI() < 28.0) \
                or self.getBodyBuild() == "Regular" and (25.0 <= self.getBMI() < 29.0) \
                or self.getBodyBuild() == "Athletic" and (25.0 <= self.getBMI() < 30.0):
            weightClassification = "Overweight"

        elif (self.getBodyBuild() == "Slim" and self.getBMI() >= 28.0) \
                or (self.getBodyBuild() == "Regular" and self.getBMI() >= 29.0) \
                or (self.getBodyBuild() == "Athletic" and self.getBMI() >= 30.0):
            weightClassification = "Obese"

        else:
            weightClassification = "Error"

        return weightClassification

    def setNumOfConditions(self):
        if self.getWeightClassification() == "Obese" or self.getWeightClassification() == "Underweight":
            self.numOfConditions += 1

        if self.hasHypertension == True:
            self.numOfConditions += 1

        if self.isAsthmatic == True or self.isSmoker == True:
            self.numOfConditions += 1

        if self.isIntubated == True:
            self.numOfConditions += 1

        if self.didRenalRT == True:
            self.numOfConditions += 1

        if self.didIntestinalSurgery == True:
            self.numOfConditions += 1

        if self.needsParenteralNutrition == True:
            self.numOfConditions += 1

    def getNumOfConditions(self):
        return self.numOfConditions

    def setReferralPriority(self):

        self.setNumOfConditions()

        if (self.isAsthmatic == True or self.isSmoker == True and self.getAge() > 55)\
                or (self.getWeightClassification() == "Obese" and self.hasHypertension == True)\
                or self.getNumOfConditions() > 2:
            self.referralPriority = 1

        elif self.getNumOfConditions() == 2:
            self.referralPriority = 2

        elif self.getNumOfConditions() < 2:
            self.referralPriority = 3

        else:
            self.referralPriority = 4

        for i in patientsList:
            i.setReferralPriority()

        for i in patientsList:
            if i.getReferralPriority() == 1:
                patientReferralList.append(i)

        for i in patientsList:
            if i.getReferralPriority() == 2:
                patientReferralList.append(i)

        for i in patientsList:
            if i.getReferralPriority() == 3:
                patientReferralList.append(i)

        for i in patientsList:
            if i.getReferralPriority() == 4:
                patientReferralList.append(i)

    def getReferralPriority(self):
        return self.referralPriority
