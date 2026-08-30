from utils import save,load
def addProduct():
    products = load("data/products.json")
    id = int(input("enter ID: "))
    for i in products:
        if i["id"] == id:
            print("can not have duplicates for IDs")
            return
    name = input("enter name: ")
    category = input("enter category: ")
    price = int(input("enter price: "))
    if price < 0:
        print("can not have negetive price!")
        return
    stock = float(input("enter stock: "))
    if stock < 0:
        print("can not have negetive stock!")
        return

    dict = {
        "id": id,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock
    }
    products.append(dict)
    save(products,"data/products.json")
    print("saved")

def deleteProduct():
    products = load("data/products.json")
    id = int(input("enter ID: "))
    for i in products:
        if i["id"] == id:
            products.remove(i)
            save(products, "data/products.json")
            print("item removed!")
            return

def editProduct():
    products = load("data/products.json")
    id = int(input("enter the ID: "))
    for i in products:
        if i["id"] == id:
            i["name"] = input("enter the new name: ")
            i["category"] = input("enter the new category: ")
            i["price"] = int(input("enter the new price: "))
            i["stock"] = int(input("enter the new stock: "))
            break
    save(products, "data/products.json")
    print("item updated")


def searchName():
    products = load("data/products.json")
    name = input("enter name: ")
    for i in products:
        if i["name"] == name:
            print(i["id"], i["name"], i["category"], i["price"], i["stock"])

def searchCat():
    products = load("data/products.json")
    cat = input("enter category: ")
    for i in products:
        if i["category"] == cat:
            print(i["id"], i["name"], i["category"], i["price"], i["stock"])

def showProducts():
    products = load("data/products.json")
    for i in products:
        print(i)

def sortPrice():
    products = load("data/products.json")
    products.sort(key= lambda i: i["price"])
    for i in products:
        print(i)

def sortStock():
    products = load("data/products.json")
    products.sort(key= lambda i: i["stock"])
    for i in products:
        print(i)
