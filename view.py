import ControllerCat, ControllerIngre, ControllerProduct, ControllerTable

controllerCAT = ControllerCat.ControllerCat()
controllerINGRE = ControllerIngre.ControllerIngre()
controllerPROD = ControllerProduct.ControllerProduct()
controllerTABLE = ControllerTable.ControllerTable()

choice = 0
while choice != 5:
    print("1-CRUD Categories")
    print("2-CRUD Products")
    print("3-CRUD Ingredients")
    print("4-Order/Table Controll")
    print("5-Exit")

    choice = int(input("Select: "))

    if choice == 1:
        choiceCat = 0
        cat = controllerCAT.chargeCategories()
        while choiceCat != 4:
            print("1-Create a category")
            print("2-Update a category")
            print("3-Delete a category")
            print("4-Exit")
            choiceCat = int(input("Select: "))
            if choiceCat == 1:
                name = input("Name of the category: ")
                desc = input("Description of the category: ")
                jason = {
                    "name": name,
                    "description": desc
                }
                result = controllerCAT.createCategory(jason)
                if result == True:
                    print("Category added")
                else:
                    print(result)

            if choiceCat == 2:
                for category in cat:
                    print("ID:",category, " - Name:", cat[category].getName(), " - Description:", cat[category].getDesc())
                idcat = int(input("Select the category you want to update: "))
                upCatChoice = 0
                name=""
                desc = ""
                while upCatChoice != 3:
                    print("1-Change the name")
                    print("2-Change the description")
                    print("3-Exit")

                    upCatChoice = int(input("Select: "))
                    if upCatChoice == 1:
                        name = input("New name: ")
                    if upCatChoice == 2:
                        desc = input("New desc: ")

                jason = {}
                jason["id"]=idcat
                if name !="":
                    jason["name"] = name
                if desc !="":
                    jason["description"] = desc
                result = controllerCAT.updateCategory(jason)
                if result ==True:
                    print("Category updated")
                else:
                    print(result)

            if choiceCat == 3:
                for category in cat:
                    print("ID:",category, " - Name:", cat[category].getName(), " - Description:", cat[category].getDesc())
                idcat = int(input("Select the category you want to delete: "))
                jason = {
                    "id": idcat
                }
                result = controllerCAT.deleteCategory(jason)
                if result ==True:
                    print("Category deleted")
                else:
                    print(result)

    if choice == 2:
        choiceProd = 0
        prod = controllerPROD.getAllProducts()
        while choiceProd != 4:
            print("1-Create a product")
            print("2-Update a product")
            print("3-Delete a product")
            print("4-Exit")
            choiceProd = int(input("Select: "))
            if choiceProd == 1:
                name = input("Name of the product: ")
                desc = input("Description of the product: ")
                price = float(input("Price of the product: "))
                available = int(input("Available?(0:False/1:True) "))
                cat = controllerCAT.chargeCategories()
                for category in cat:
                    print("ID:",category, " - Name:", cat[category].getName(), " - Description:", cat[category].getDesc())
                idcat = int(input("Select the category for the product: "))
                ingre = controllerINGRE.chargeIngredients()
                ingres = []
                idingre = -1
                while idingre !=0:
                    for ingredient in ingre:
                        print("ID:",ingredient, " - Name:", ingre[ingredient].getName(), " - Gluten free:", ingre[ingredient].getGluten())
                    print("Press 0 to exit")
                    idingre = int(input("Select the ingredients of the product: "))
                    if idingre ==0:break
                    ingres.append(idingre)
                jason = {
                    "name": name,
                    "description": desc,
                    "price":price,
                    "category":category,
                    "ingredients":ingres
                }
                if available == 1:
                    jason["available"]=True
                if available == 0:
                    jason["available"]=False
                result = controllerPROD.createProduct(jason)
                if result == True:
                    print("Prouct added")
                else:
                    print(result)

            if choiceProd == 2:
                for product in prod:
                    print("ID:",product, " - Name:", prod[product].getName(), " - Price:", prod[product].getPrice())
                idprod = int(input("Select the product you want to update: "))
                upProdChoice = 0
                name=""
                desc = ""
                price=0
                available=""
                category=0
                ingredients=[]
                while upProdChoice != 7:
                    print("1-Change the name")
                    print("2-Change the description")
                    print("3-Change the price")
                    print("4-Change the availability")
                    print("5-Change the category")
                    print("6-Change the ingredients")
                    print("7-Finish editing")
                    upProdChoice = int(input("Select: "))
                    if upProdChoice == 1:
                        name = input("New name: ")
                    if upProdChoice == 2:
                        desc = input("New desc: ")
                    if upProdChoice == 3:
                        price = float(input("New price: "))
                    if upProdChoice == 4:
                        available = int(input("New availability(0:False/1:True): "))
                    if upProdChoice == 5:
                        cat = controllerCAT.chargeCategories()
                        for category in cat:
                            print("ID:",category, " - Name:", cat[category].getName(), " - Description:", cat[category].getDesc())
                        category = int(input("New category: "))
                    if upProdChoice == 6:
                        ingre = controllerINGRE.chargeIngredients()
                        idingre = -1
                        while idingre !=0:
                            for ingredient in ingre:
                                print("ID:",ingredient, " - Name:", ingre[ingredient].getName(), " - Gluten free:", ingre[ingredient].getGluten())
                            print("Press 0 to exit")
                            idingre = int(input("Select the ingredients of the product: "))
                            if idingre ==0:break
                            ingredients.append(idingre)

                jason = {}
                jason["id"]=idprod
                if name !="":
                    jason["name"] = name
                if desc !="":
                    jason["description"] = desc
                if price>0:
                    jason["price"] = price
                if available == 1:
                    jason["available"]=True
                if available == 0:
                    jason["available"]=False
                if category>0:
                    jason["category"] = category
                if len(ingredients) >0:
                    jason["ingredients"]=ingredients
                result = controllerPROD.updateProduct(jason)
                if result ==True:
                    print("Product updated")
                else:
                    print(result)

            if choiceProd == 3:
                for product in prod:
                    print("ID:",product, " - Name:", prod[product].getName(), " - Price:", prod[product].getPrice())
                idprod = int(input("Select the product you want to delete: "))
                jason = {
                    "id": idprod
                }
                result = controllerPROD.deleteProduct(jason)
                if result ==True:
                    print("Product deleted")
                else:
                    print(result)

    if choice == 3:
        choiceIngre = 0
        ingre = controllerINGRE.chargeIngredients()
        while choiceIngre != 4:
            print("1-Create an ingredient")
            print("2-Update an ingredient")
            print("3-Delete an ingredient")
            print("4-Exit")
            choiceIngre = int(input("Select: "))
            if choiceIngre == 1:
                name = input("Name of the ingredient: ")
                gluten = int(input("Gluten free(0:False/1:True): "))
                obs = input("Any observation?" )
                jason = {
                    "name": name,
                }
                if gluten == 1:
                    jason["gluten"]=True
                if gluten == 0:
                    jason["gluten"]=False
                if len(obs) >0 or obs != None:
                    jason["observations"] = obs
                result = controllerINGRE.createIngredient(jason)
                if result == True:
                    print("Ingredtient added")
                else:
                    print(result)

            if choiceIngre == 2:
                for ingredient in ingre:
                    print("ID:",ingredient, " - Name:", ingre[ingredient].getName(), " - Gluten free:", ingre[ingredient].getGluten())
                idingre = int(input("Select the ingredient you want to update: "))
                upIngreChoice = 0
                observations=""
                name=""
                gluten=""
                while upIngreChoice != 4:
                    print("1-Change the name")
                    print("2-Change the gluten option")
                    print("3-Change the observations")
                    print("4-Exit")

                    upIngreChoice = int(input("Select: "))
                    if upIngreChoice == 1:
                        name = input("New name: ")
                    if upIngreChoice == 2:
                        gluten = int(input("New gluten option(0:False/1:True): "))
                    if upIngreChoice == 3:
                        observations = input("New Observations: ")

                jason = {}
                jason["id"]=idingre
                if name !="":
                    jason["name"] = name
                if gluten == 1:
                    jason["gluten"]=True
                if gluten == 0:
                    jason["gluten"]=False
                if observations != "":
                    jason["observations"] = observations
                result = controllerINGRE.updateIngredient(jason)
                if result ==True:
                    print("Ingredient updated")
                else:
                    print(result)

            if choiceIngre == 3:
                for ingredient in ingre:
                    print("ID:",ingredient, " - Name:", ingre[ingredient].getName(), " - Gluten free:", ingre[ingredient].getGluten())
                idingre = int(input("Select the ingredient you want to delete: "))
                jason = {
                    "id": idingre
                }
                result = controllerINGRE.deleteIngredient(jason)
                if result ==True:
                    print("Ingredient deleted")
                else:
                    print(result)

    if choice == 4:
        choiceTable = 0
        tables = controllerTABLE.chargeTable()
        while choiceTable != 7:
            print("1-Create a table")
            print("2-Update a table")
            print("3-Finish a table")
            print("4-List all tables")
            print("5-Take an order for a table")
            print("6-Edit order list")
            print("7-Exit")
            choiceTable = int(input("Select: "))
            if choiceTable == 1:
                num = int(input("Num of the table: "))
                diners = int(input("Number of diners: "))
                waiter = input("Waiter name: ")
                client = input("Client name: ")
                jason = {
                    "num": num,
                    "diners":diners,
                    "client":client,
                    "waiter":waiter
                    
                }
                result = controllerTABLE.createTable(jason)
                if result == True:
                    print("Table added")
                else:
                    print(result)

            if choiceTable == 2:
                for table in tables:
                    if tables[table].getState() != "F":
                        print("ID:",table, " - Num:", tables[table].getNum(), " - Diners:", tables[table].getDiners(), " - Waiter:", tables[table].getWaiter(), " - State:", tables[table].getState())
                idTable = int(input("Select the table you want to update: "))
                upTableChoice = 0
                num = 0
                diners = 0
                waiter = ""
                client = ""
                state = ""
                while upTableChoice != 6:
                    print("1-Change the num")
                    print("2-Change the number of diners")
                    print("3-Change the waiter")
                    print("4-Change the client")
                    print("5-Change the state(W:Waiting/E:Eating)")
                    print("6-Exit")
                    upTableChoice = int(input("Select: "))
                    if upTableChoice == 1:
                        num = int(input("New num: "))
                    if upTableChoice == 2:
                        diners = int(input("Number of diners: "))
                    if upTableChoice == 3:
                        waiter = input("New waiter: ")
                    if upTableChoice == 4:
                        client = input("New client name: ")
                    if upTableChoice == 5:
                        state = input("New state(W:Waiting/E:Eating): ")

                jason = {}
                jason["id"]=idTable
                if num !=0:
                    jason["num"] = num
                if diners != 0:
                    jason["diners"]=diners
                if waiter != "":
                    jason["waiter"]=waiter
                if client !="":
                    jason["client"] = client
                if state =="W":
                    jason["state"] = state
                if state =="E":
                    jason["state"] = state
                if state != "W" and state != "E":
                    print("The state value is not correct, no changes made in the state")
                result = controllerTABLE.updateTable(jason)
                if result ==True:
                    print("Table updated")
                else:
                    print(result)

            if choiceTable == 3:
                for table in tables:
                    if tables[table].getState() != "F":
                        print("ID:",table, " - Num:", tables[table].getNum(), " - Diners:", tables[table].getDiners(), " - Waiter:", tables[table].getWaiter(), " - State:", tables[table].getState())
                idTable = int(input("Select the table you want to update: "))
                jason = {
                    "id": idTable,
                    "state":"F"
                }
                result = controllerTABLE.finishTable(jason)
                if result ==True:
                    print("Table finished")
                else:
                    print(result)

            if choiceTable == 4:
                for table in tables:
                    if tables[table].getState() != "F":
                        print("ID:",table, " - Num:", tables[table].getNum(), " - Diners:", tables[table].getDiners(), " - Waiter:", tables[table].getWaiter(), " - State:", tables[table].getState(), " - Total:", tables[table].getTotal())
                        if len(tables[table].getOrder())>0:
                            for order in tables[table].getOrder():
                                print("\t",tables[table].getOrder()[order].getQuant()," - ",tables[table].getOrder()[order].getProduct().getName()," - ",tables[table].getOrder()[order].getPrice())
                        else:
                            print("This table has not ordered nothing")

            if choiceTable == 5:
                for table in tables:
                    if tables[table].getState() != "F":
                        print("ID:",table, " - Num:", tables[table].getNum(), " - Diners:", tables[table].getDiners(), " - Waiter:", tables[table].getWaiter(), " - State:", tables[table].getState(), " - Total:", tables[table].getTotal())
                        if len(tables[table].getOrder())>0:
                            for order in tables[table].getOrder():
                                print("\t",tables[table].getOrder()[order].getQuant()," - ",tables[table].getOrder()[order].getProduct().getName()," - ",tables[table].getOrder()[order].getPrice())
                        else:
                            print("This table has not ordered anything")
                idTable = int(input("Select the table: "))
                
                filterCat = 0
                cat = controllerCAT.chargeCategories()
                while filterCat != (len(cat)+1):
                    for category in cat:
                        print(category," - ",cat[category].getName())
                    print((len(cat)+1),"-Exit")
                    filterCat = int(input("Select the category: "))
                    if filterCat == (len(cat)+1): break

                    prod = controllerPROD.getAllProducts()
                    for product in prod:
                        if prod[product].getCategory().getName() ==controllerCAT.findCategory(filterCat).getName():
                            print(product," - ",prod[product].getName()," - ",prod[product].getPrice())

                    idProd = int(input("Select the plate: "))
                    quant = int(input("How many plates: "))
                    jason = {
                        "numTable":idTable,
                        "quant":quant,
                        "product":idProd
                    }

                    result = controllerTABLE.addOrder(jason)
                    if result ==True:
                        print("Order added")
                    else:
                        print(result)
                    
            if choiceTable == 6:
                for table in tables:
                    if len(tables[table].getOrder())>0:
                        print("ID:",table, " - Num:", tables[table].getNum(), " - Diners:", tables[table].getDiners(), " - Waiter:", tables[table].getWaiter(), " - State:", tables[table].getState(), " - Total:", tables[table].getTotal())
                idTable = int(input("Select the table: "))

                editOrder = 0
                while editOrder != 3:
                    print("1-Update an order")
                    print("2-Delete an order")
                    print("3-Exit")
                    
                    editOrder=int(input("Select an option: "))
                    if editOrder == 1:
                        for order in tables[idTable].getOrder():
                            print("Id:",order," -Quant",tables[idTable].getOrder()[order].getQuant()," - ",tables[idTable].getOrder()[order].getProduct().getName()," - ",tables[idTable].getOrder()[order].getPrice())
                        idOrder = int(input("Select the order you want to change: "))

                        upOrder = 0
                        quant = 0
                        observations = ""
                        while upOrder !=3:
                            print("1-Change the quantity")
                            print("2-Change the observations")
                            print("3-Exit")

                            upOrder = int(input("Select: "))

                            if upOrder == 1:
                                quant = int(input("New quantity: "))
                            if upOrder == 2:
                                observations = input("New observations: ")

                            jason = {
                                "id":idOrder
                            }
                            if quant != 0:
                                jason["quant"] = quant
                            if observations != "":
                                jason["observations"] = observations
                            result = controllerTABLE.updateOrder(jason, idTable)
                            if result == True:
                                print("Order updated")
                            else:
                                print(result)
                    
                    if editOrder == 2:
                        for order in tables[idTable].getOrder():
                            print("Id:",order," -Quant",tables[idTable].getOrder()[order].getQuant()," - ",tables[idTable].getOrder()[order].getProduct().getName()," - ",tables[idTable].getOrder()[order].getPrice())
                        idOrder = int(input("Select the order you want to delete: "))
                        jason={
                            "id":idOrder
                        }
                        result = controllerTABLE.deleteOrder(jason,idTable)
                        if result == True:
                            print("Order deleted")
                        else:
                            print(result)

                            