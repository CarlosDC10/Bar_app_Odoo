class Category:
    def __init__(self,name,description) -> None:
        self.__name = name
        self.__description = description

    def getName(self):
        return self.__name
    
    def getDesc(self):
        return self.__description

    def setName(self,name):
        self.__name = name
    
    def setDesc(self,desc):
        self.__description = desc