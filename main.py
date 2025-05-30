from helper.postgresConnection import postgresConnection
from view.auth_view import registrasi, tampilkan_data, update_data, delete_data
import os
if __name__ == "__main__" :
    while True:
        print("SELAMAT DATANG DI SOLARIA")
        print("1. Tampilkan Data")
        print("2. Tambah Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Exit")
        pilihan = int(input("Masukkan pilihanmu : ").strip())
        
        if (pilihan == 1):
            tampilkan_data()
        
        elif (pilihan == 2):
            registrasi()
        elif (pilihan == 3):
            update_data()
        elif (pilihan == 4):
            delete_data()
        else:
            os._exit()