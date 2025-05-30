import psycopg2
def postgresConnection():
    try:
        conn = psycopg2.connect(
            dbname = "projek_akhir",
            port = 5432,
            host = "localhost",
            user = "postgres",
            password = "root"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error Koneksi ke database ❌: {e}")