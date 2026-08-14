from products import addProduct
data = int(input("what data do ypu want to change?\n 1.products\n 2.orders\n 3.users: "))
if data == 2:
    with open("products.py", "r") as f:
        order = int(input("how can I help?\n 1.add\n 2.delete\n 3.edit\n 4.search by name\n 5.search by category\n 6.show all products"))
        if order == 1:
            addProduct()