class Order:
    def __init__(self, product, quant, price,observations) -> None:
        self.__product = product
        self.__quant = quant
        self.__price = price
        self.__observations = observations

    def getProduct(self):
        return self.__product

    def getQuant(self):
        return self.__quant
    
    def getPrice(self):
        return self.__price

    def getObservations(self):
        return self.__observations

    def setProduct(self,product):
        self.__product = product

    def setQuant(self,quant):
        self.__quant = quant
    
    def setPrice(self,price):
        self.__price = price
    
    def setObservations(self,obs):
        self.__observations = obs