import products, orders, users, reports
def menu():
    print("========== Online Store =========")
    print("1.products\n 2.users\n 3.orders \n 4.reports\n 5.exit")
    print("=================================")

def productMenu():
    print("========== products =========")
    print("1.add product\n 2.delete product\n 3.edit product\n 4.search by name\n 5.search by category\n 6.show products\n 7.sort by price\n 8.sort by stocking\n 9.exit")
    print("=================================")

def userMenu():
    print("========== users =========")
    print("1.add user\n 2.delete user\n 3.edit user\n 4.search user\n 5.show users\n 6.exit")
    print("=================================")

def orderMenu():
    print("========== orders =========")
    print("1.add order\n 2.delete order\n 3.calculate total\n 4.update stocking\n 5.show orders\n 6.exit")
    print("=================================")

def reportMenu():
    print("========== reports =========")
    print("1.products value\n 2.products\n 3.customers\n 4.VIPs\n 5.orders\n 6.out of stock\n 7.less than 5 stockings\n 8.most expensive\n 9.cheapest\n 10.avrage price\n 11.exit")
    print("=================================")

while True:
    menu()
    option = int(input("what to access: "))
    if option == 1:
        while True:
            productMenu()
            access = int(input("enter: "))
            if access == 1:
                products.addProduct()
            elif access == 2:
                products.deleteProduct()
            elif access == 3:
                products.editProduct()
            elif access == 4:
                products.searchName()
            elif access == 5:
                products.searchCat()
            elif access == 6:
                products.showProducts()
            elif access == 7:
                products.sortPrice()
            elif access == 8:
                products.sortStock()
            elif access == 9:
                menu()

    elif option == 2:
        while True:
            userMenu()
            access = int(input("enter: "))
            if access == 1:
                users.addUser()
            elif access == 2:
                users.deleteUser()
            elif access == 3:
                users.editUser()
            elif access == 4:
                users.searchUser()
            elif access == 5:
                users.showUsers()
            elif access == 6:
                menu()

    elif option == 3:
        while True:
            orderMenu()
            access = int(input("enter: "))
            if access == 1:
                orders.addOrder()
            elif access == 2:
                orders.deleteOrder()
            elif access == 3:
                print("something went wrong! try again later.")
            elif access == 4:
                print("something went wrong! try again later.")
            elif access == 5:
                orders.showOrder()
            elif access == 6:
                menu()

    elif option == 4:
        while True:
            reportMenu()
            access = int(input("enter: "))
            if access == 1:
                reports.productsValue()
            elif access == 2:
                reports.allProducts()
            elif access == 3:
                reports.allCustomers()
            elif access == 4:
                reports.allVip()
            elif access == 5:
                reports.allOrders()
            elif access == 6:
                reports.outOfStock()
            elif access == 7:
                reports.stock_5()
            elif access == 8:
                reports.expensive()
            elif access == 9:
                reports.cheap()
            elif access == 10:
                reports.avgPrice()
            elif access == 11:
                menu()
