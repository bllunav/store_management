from utils import load
products = load("data/products.json")
users = load("data/users.json")
orders = load("data/orders.json")
def productsValue():
    cnt = 0
    for i in products:
        cnt += i["price"]

    print(f"value: {cnt}")

def allProducts():
    cnt = 0
    for i in products:
        cnt += 1
    print(f"number of products: {cnt}")

def allCustomers():
    cnt = 0
    for i in users:
        cnt += 1
    print(f"number of customers: {cnt}")

def allVip():
    cnt = 0
    for i in users:
        if i["vip"] == True:
            cnt +=1
    print(f"number of VIPs: {cnt}")

def allOrders():
    cnt = 0
    for i in orders:
        cnt += 1
    print(f"number of orders: {cnt}")

def outOfStock():
    cnt = 0
    for i in products:
        if i["stock"] == 0:
            cnt += 1
    print(f"out of stock items: {cnt}")

def stock_5():
    cnt = 0
    for i in products:
        if i["stock"] < 5:
            cnt += 1
    print(f"less than five in stock: {cnt}")     

def expensive():
    product = sorted(products, key=lambda i: i["price"], reverse=True)
    print(f"the most expensive item: {product[0]}")

def cheap():
    product = sorted(products, key= lambda i: i["price"])
    print(f"the cheapest item: {product[0]}")

def avgPrice():
    cnt = 0
    len = 0
    for i in products:
        cnt += i["price"]
        len += 1
    print(f"avrage price of products: {cnt/len}")

# def catProducts():

# def mostOrder():

# def mostSold():