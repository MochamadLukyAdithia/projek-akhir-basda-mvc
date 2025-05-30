from controller.AkunController import create, read, update, delete
from model.Akun import Akun
from tabulate import tabulate
def registrasi():
    print ("=========MENU REGISTRASI========")
    username = input("Masukkan Username : ").strip()
    password = input("Masukkan Password : ").strip()
    user = Akun(
        username = username,
        password = password
    )
    create(user)
    
def tampilkan_data():
    print ("=========MENU DATA AKUN========")
    users = read()
    table = [
        [data["id"],
        data["username"],
        data["password"]] for data in users
    ]
    headers = [
        "ID",
        "USERNAME",
        "PASSWORD"
    ]
    print(tabulate(table, headers=headers, tablefmt="grid"))
    
def update_data():
    print ("=========MENU UPDATE========")
    tampilkan_data()
    id = int(input("Masukkan ID : ").strip())
    username = str(input("Masukkan Username : ").strip())
    update(username, id)
    tampilkan_data()
    
def delete_data():
    print ("=========MENU DELETE========")
    tampilkan_data()
    id = int(input("Masukkan ID : ").strip())
    delete(id)
    tampilkan_data()