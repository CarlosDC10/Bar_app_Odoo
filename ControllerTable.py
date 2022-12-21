import json
import requests
from Table import Table
from Order import Order
import ControllerOrder

controllerORDER = ControllerOrder.ControllerOrder()

class ControllerTable:

    def __init__(self) -> None:
        self.__tables = {}

    def createTable(self, jason):
        response = requests.post("http://localhost:8069/bar_app/addTable",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 201:
            self.__tables[response["result"]["id"]] = Table(jason["num"],jason["diners"],jason["waiter"],jason["client"])
            return True
        else:
            return (response)

    def updateTable(self, jason):
        response = requests.put("http://localhost:8069/bar_app/updateTable",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 201:
            if "num" not in jason: jason["num"] = self.__tables[response["result"]["id"]].getNum()
            if "diners" not in jason: jason["diners"] = self.__tables[response["result"]["id"]].getDiners()
            if "waiter" not in jason: jason["waiter"] = self.__tables[response["result"]["id"]].getWaiter()
            if "client" not in jason: jason["client"] = self.__tables[response["result"]["id"]].getClient()
            if "state" not in jason: jason["state"] = self.__tables[response["result"]["id"]].getState()
            if "total" not in jason: jason["total"] = self.__tables[response["result"]["id"]].getTotal()
            if "products" not in jason: jason["products"] = self.__tables[response["result"]["id"]].getOrder()
            self.__tables[response["result"]["id"]] = Table(jason["num"],jason["diners"],jason["waiter"],jason["client"])
            self.__tables[response["result"]["id"]].setState(jason["state"])
            self.__tables[response["result"]["id"]].setTotal(jason["total"])
            self.__tables[response["result"]["id"]].setOrder(jason["products"])
            return True
        else:
            return (response)

    def finishTable(self, jason):
        response = requests.delete("http://localhost:8069/bar_app/updateTable",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 201:
            self.__tables[response["result"]["id"]].setState("F")
            return True
        else:
            return response

    def chargeTable(self):
        response = requests.request("GET", "http://localhost:8069/bar_app/getTable")
        if response.status_code == 200:
            data = response.json()
            for num in range(len(data["data"])):
                id = data["data"][num]["id"]
                numTable=data["data"][num]["num"]
                diners = data["data"][num]["diners"]
                waiter = data["data"][num]["waiter"]
                client = data["data"][num]["waiter"]
                state = data["data"][num]["state"]
                c = Table(numTable,diners,waiter,client)
                orders = {}
                total = 0
                for order in data["data"][num]["products"]:
                    orders[order] = controllerORDER.findOrder(order)
                    total = total + orders[order].getPrice()
                c.setOrder(orders)
                c.setState(state)
                c.setTotal(total)
                self.__tables[id] = c
        return self.__tables

    def getTables(self):
        return self.__tables

    def addOrder(self, jason):
        response = requests.post("http://localhost:8069/bar_app/addOrder",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 201:
            self.__tables[jason["numTable"]].getOrder()[response["result"]["id"]] = controllerORDER.findOrder(response["result"]["id"])
            total = 0
            for order in self.__tables[jason["numTable"]].getOrder():
                    total = total + self.__tables[jason["numTable"]].getOrder()[order].getPrice()
            self.__tables[jason["numTable"]].setTotal(total)
            return True
        else:
            return (response)

    def updateOrder(self, jason, idTable):
        response = requests.put("http://localhost:8069/bar_app/updateOrder",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 201:
            jason["product"] = self.__tables[idTable].getOrder()[response["result"]["id"]].getProduct()
            if "quant" not in jason: jason["quant"] = self.__tables[idTable].getOrder()[response["result"]["id"]].getQuant()
            if "observations" not in jason: jason["observations"] = self.__tables[idTable].getOrder()[response["result"]["id"]].getObservations()
            jason["price"] = jason["product"].getPrice() * jason["quant"]
            self.__tables[idTable].getOrder()[response["result"]["id"]] = Order(jason["product"],jason["quant"],jason["price"],jason["observations"])
            total = 0
            for order in self.__tables[idTable].getOrder():
                    total = total + self.__tables[idTable].getOrder()[order].getPrice()
            self.__tables[idTable].setTotal(total)
            return True
        else:
            return (response)

    def deleteOrder(self, jason,idTable):
        response = requests.delete("http://localhost:8069/bar_app/deleteOrder",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 200:
            del self.__tables[idTable].getOrder()[jason["id"]]
            total = 0
            for order in self.__tables[idTable].getOrder():
                    total = total + self.__tables[idTable].getOrder()[order].getPrice()
            self.__tables[idTable].setTotal(total)
            return True
        else:
            return response