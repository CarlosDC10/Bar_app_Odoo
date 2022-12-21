class Table:
    def __init__(self,num,diners,waiter,client) -> None:
        self.__num = num
        self.__diners = diners
        self.__waiter = waiter
        self.__client = client
        self.__state = "W"
        self.__order = {}
        self.__total = 0
    
    def getNum(self):
        return self.__num

    def getOrder(self):
        return self.__order
    
    def setNum(self,num):
        self.__num = num

    def setOrder(self,order):
        self.__order = order

    def getDiners(self):
        return self.__diners

    def setDiners(self,diners):
        self.__diners = diners

    def getWaiter(self):
        return self.__waiter

    def setDiners(self,waiter):
        self.__waiter = waiter
    
    def getClient(self):
        return self.__client

    def setDiners(self,client):
        self.__client = client

    def getTotal(self):
        return self.__total

    def setTotal(self,total):
        self.__total = total

    def getState(self):
        return self.__state

    def setState(self,state):
        self.__state = state