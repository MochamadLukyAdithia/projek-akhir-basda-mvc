from model.Akun import Akun
from helper.postgresConnection import postgresConnection as db


def create(user: Akun):
    try:
        conn = db()
        cursor = conn.cursor()
        query = "INSERT INTO akun (username, password) VALUES (%s, %s)"
        cursor.execute(query, (user.username, user.password))
        conn.commit()
        print("Registrasi Succes ✅")
    except Exception as e:
           print(f"Registrasi Gagal {e}")
    finally:
         cursor.close()
         conn.close()


def read():
    try:
        conn = db()
        cursor = conn.cursor()
        query = "SELECT * FROM akun"
        cursor.execute(query)
        users = cursor.fetchall()
        return [
             {
                  "id" : user[0],
                  "username" : user[1],
                  "password" : user[2]
             } for user in users
        ]
    except Exception as e:
           return None
    finally:
         cursor.close()
         conn.close()


def update(username, id):
    try:
        conn = db()
        cursor = conn.cursor()
        query = "UPDATE akun SET username = %s WHERE id = %s"
        cursor.execute(query, (username, id))
        conn.commit()
        print("Update Berhasil")
    except Exception as e:
         print("Update Gagal")
    finally:
         cursor.close()
         conn.close()
         
def delete(id):
    try:
        conn = db()
        cursor = conn.cursor()
        query = "DELETE FROM akun WHERE id = %s"
        cursor.execute(query, (id, ))
        conn.commit()
        print("Delete Berhasil")
    except Exception as e:
         print("Delete Gagal")
    finally:
         cursor.close()
         conn.close()