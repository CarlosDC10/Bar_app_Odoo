class Product:
    def __init__(self,name,description,price, available) -> None:
        self.__name = name
        self.__description = description
        self.__price = price
        self.__available = available
        self.__category = None
        self.__ingredients = []

    def getName(self):
        return self.__name
    
    def getDesc(self):
        return self.__description

    def getPrice(self):
        return self.__price

    def getAvailable(self):
        return self.__available

    def getCategory(self):
        return self.__category

    def getIngredients(self):
        return self.__ingredients

    def setName(self,name):
        self.__name = name
    
    def setDesc(self,desc):
        self.__description = desc

    def setPrice(self,price):
        self.__price = price

    def setAvailable(self,available):
        self.__available = available

    def setCategory(self,category):
        self.__category = category

    def setIngredients(self,ingre):
        self.__ingredients = ingre