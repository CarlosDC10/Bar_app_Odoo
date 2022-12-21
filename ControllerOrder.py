import requests, json
from Order import Order
import ControllerProduct

contrllerProduct = ControllerProduct.ControllerProduct()

class ControllerOrder:
     
    def __init__(self) -> None:
        pass

    def findOrder(self,id):
        response = requests.request("GET", "http://localhost:8069/bar_app/getOrder/"+str(id))
        if response.status_code == 200:
            data = response.json()
            for num in range(len(data["data"])):
                product = contrllerProduct.findProduct(data["data"][num]["product"][0])
                quant = data["data"][num]["quant"]
                price = data["data"][num]["price"]
                observations = data["data"][num]["observations"]
                c = Order(product,quant,price,observations)
                return c
