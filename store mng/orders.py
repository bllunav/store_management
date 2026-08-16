from utils import save,load
orders = load("data/orders.json")
def addOrder():
    order = int(input("enter ID: "))
    for i in orders:
        if i["order"] == order:
            print("can not have duplicates for IDs")
            return
    customer = input("enter customer: ")
    number = int(input("how many products? "))
    product_name = []
    quantity = []
    product_lst = []
    for i in range(0,number):
        product_name = input("enter product name: ")
        quantity = int(input("enter quantity: "))
        products= {"product_name": product_name,
                   "quantity": quantity}
        product_lst.append(products)
    total = float(input("enter total: "))

    dict = {
        "order": order,
        "customer": customer,
        "products": product_lst,
        "total": total
    }
    orders.append(dict)
    save(orders,"data/orders.json")
    print("saved")
    
def deleteOrder():
    order = int(input("enter ID: "))
    for i in orders:
        if i["order"] == order:
            orders.remove(i)
            save(orders, "data/orders.json")
            print("order canclled!")
            return

def showOrder():
    order = int(input("1.show all  2.search by name: "))
    if order == 1:
        for i in orders:
            print(f"customer: {i["customer"]}\n", f"order: {i["products"]}")
    if order == 2:
        name = input("enter name: ")
        for i in orders:
            if i["customer"] == name:
                print(f"customer: {i["customer"]}\n", f"order: {i["products"]}")
                break
