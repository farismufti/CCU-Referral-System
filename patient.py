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

    def isSmoker(self, isSmoker):
        return self.isSmoker

    def isAsthmatic(self, isAsthmatic):
        return self.isAsthmatic

    def isIntubated(self, isIntubated):
        return self.isIntubated

    def hasHypertension(self, hasHypertension):
        return self.hasHypertension

    def didRenalRT(self, didRenalRT):
        return self.didRenalRT

    def didIntestinalSurgery(self, didIntestinalSurgery):
        return self.didIntestinalSurgery

    def needsParenteralNutrition(self, needsParenteralNutrition):
        return self.needsParenteralNutrition

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
