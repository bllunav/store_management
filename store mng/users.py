from utils import load,save
def addUser():
    users = load("data/users.json")
    id = int(input("enter id: "))
    for i in users:
        if i["id"] == id:
            print("can not have duplicates for IDs")
            return
    name = input("enter name: ")
    phone = str(input("enter the phone: "))
    cnt = 0
    for i in phone:
        cnt+=1
    if cnt != 11:
        print("wrong number")
        return
    city = input("enter city: ")
    vip = bool(input("vip state - true/false: "))

    dic = {
        "id": id,
        "name": name,
        "phone": phone,
        "city": city,
        "vip": vip
    },

    users.append(dic)
    save(users, "data/users.json")
    print("saved")

# not working
def deleteUser():
    users = load("data/users.json")
    id = int(input("enter ID: "))
    for i in users:
        if i["id"] == id:
            users.remove(i)
            save(users, "data/users.json")
            print("user removed!")
            return

def delete_user():
    users = load("data/users.json")
    user_id = int(input("Enter user ID: "))
    for i in users:
        if i["id"] == user_id:
            users.remove(i)
            save(users, "data/users.json")
            print("User deleted successfully!")
            return
    print("User not found!")

def editUser():
    users = load("data/users.json")
    id = int(input("enter the ID: "))
    for i in users:
        if i["id"] == id:
            i["name"] = input("enter the new name: ")
            i["phone"] = input("enter new phone: ")
            i["city"] = input("enter the new city: ")
            i["vip"] = bool(input("new vip state - true/false: "))
            break
    save(users, "data/users.json")
    print("user updated")

def searchUser():
    users = load("data/users.json")
    id = int(input("enter ID: "))
    for i in users:
        if i["id"] == id:
            print(i["id"], i["name"], i["phone"], i["city"], i["vip"])

def showUsers():
    users = load("data/users.json")
    for i in users:
        print(i)