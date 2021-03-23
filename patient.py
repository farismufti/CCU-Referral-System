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
        BMI = 0

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
        BMI = self.getWeight() / (self.getHeight() ** 2)
        return round(float(BMI), 1)

    def getWeightClassification(self):
        if self.getBMI() < 18.5:
            weightClassification = "Underweight"

        elif self.getBMI() == 18.5 or self.getBMI() < 25:
            weightClassification = "Normal"

        elif self.getBodyBuild() == "Slim" and (self.getBMI() >= 25 or self.getBMI() < 28)\
                or self.getBodyBuild() == "Regular" and (self.getBMI() >= 25 or self.getBMI() < 29)\
                or self.getBodyBuild() == "Athletic" and (self.getBMI() >= 25 or self.getBMI() < 30):
            weightClassification = "Overweight"

        else:
            weightClassification = "Obese"

        return weightClassification
