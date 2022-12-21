import json
import requests
from Ingredient import Ingredient


class ControllerIngre:

    def __init__(self) -> None:
        self.__ingredients = {}

    def createIngredient(self, jason):
        response = requests.post("http://localhost:8069/bar_app/addIngredient",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 201:
            self.__ingredients[response["result"]["id"]] = Ingredient(jason["name"],jason["gluten"],jason["observations"])
            return True
        else:
            return (response)

    def updateIngredient(self, jason):
        response = requests.put("http://localhost:8069/bar_app/updateIngredient",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 201:
            if "name" not in jason: jason["name"] = self.__ingredients[response["result"]["id"]].getName()
            if "gluten" not in jason: jason["gluten"] = self.__ingredients[response["result"]["id"]].getGluten()
            if "observations" not in jason: jason["observations"] = self.__ingredients[response["result"]["id"]].getDesc()
            self.__ingredients[response["result"]["id"]] = Ingredient(jason["name"],jason["gluten"],jason["observations"])
            return True
        else:
            return (response)

    def deleteIngredient(self, jason):
        response = requests.delete("http://localhost:8069/bar_app/deleteIngredient",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 200:
            del self.__ingredients[jason["id"]]
            return True
        else:
            return response

    def chargeIngredients(self):
        response = requests.request("GET", "http://localhost:8069/bar_app/getIngredient")
        if response.status_code == 200:
            data = response.json()
            for num in range(len(data["data"])):
                id = data["data"][num]["id"]
                name=data["data"][num]["name"]
                gluten = data["data"][num]["gluten"]
                observations = data["data"][num]["observations"]
                c = Ingredient(name,gluten,observations)
                self.__ingredients[id] = c
        return self.__ingredients

    def getIngredients(self):
        return self.__ingredients

    def findIngredient(self, id):
        response = requests.request("GET", "http://localhost:8069/bar_app/getIngredient/"+str(id))
        if response.status_code == 200:
            data = response.json()
            for num in range(len(data["data"])):
                if data["data"][num]["id"] in self.__ingredients: return self.__ingredients[data["data"][num]["id"]]
                else:
                    name = data["data"][num]["name"]
                    gluten = data["data"][num]["gluten"]
                    observation = data["data"][num]["observations"]
                    c = Ingredient(name,gluten,observation)
                    self.__ingredients[id] = c
                    return c