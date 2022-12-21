import json
import requests
from Category import Category

class ControllerCat:

    def __init__(self) -> None:
        self.__categories = {}

    def createCategory(self, jason):
        response = requests.post("http://localhost:8069/bar_app/addCategory",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 201:
            self.__categories[response["result"]["id"]] = Category(jason["name"],jason["description"])
            return True
        else:
            return (response)

    def updateCategory(self, jason):
        response = requests.put("http://localhost:8069/bar_app/updateCategory",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 201:
            if "name" not in jason: jason["name"] = self.__categories[response["result"]["id"]].getName()
            if "description" not in jason: jason["description"] = self.__categories[response["result"]["id"]].getDesc()
            self.__categories[response["result"]["id"]] = Category(jason["name"],jason["description"])
            return True
        else:
            return (response)

    def deleteCategory(self, jason):
        response = requests.delete("http://localhost:8069/bar_app/deleteCategory",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 200:
            del self.__categories[jason["id"]]
            return True
        else:
            return response

    def chargeCategories(self):
        response = requests.request("GET", "http://localhost:8069/bar_app/getCategory")
        if response.status_code == 200:
            data = response.json()
            for num in range(len(data["data"])):
                id = data["data"][num]["id"]
                name=data["data"][num]["name"]
                desc = data["data"][num]["description"]
                c = Category(name,desc)
                self.__categories[id] = c
        return self.__categories

    def getCategories(self):
        return self.__categories

    def findCategory(self,id):
        response = requests.request("GET", "http://localhost:8069/bar_app/getCategory/"+str(id))
        if response.status_code == 200:
            data = response.json()
            for num in range(len(data["data"])):
                if data["data"][num]["id"] in self.__categories: return self.__categories[data["data"][num]["id"]]
                else:
                    name = data["data"][num]["name"]
                    desc = data["data"][num]["description"]
                    c = Category(name,desc)
                    self.__categories[id] = c
                    return c