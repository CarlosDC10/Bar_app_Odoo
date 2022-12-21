class Ingredient:
    def __init__(self,name,gluten,observations) -> None:
        self.__name = name
        self.__gluten = gluten
        self.__observations = observations

    def getName(self):
        return self.__name

    def getGluten(self):
        return self.__gluten

    def getDesc(self):
        return self.__observations

    def setName(self,name):
        self.__name = name

    def setName(self,gluten):
        self.__gluten = gluten
    
    def setDesc(self,desc):
        self.__observations = desc