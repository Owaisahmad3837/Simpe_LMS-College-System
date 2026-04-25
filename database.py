import psycopg2

def get_conn():
    conn = psycopg2.connect(
        host="localhost",
        database="school_db",
        user="owais",
        password="owais7383",
        port="5432"
    )
    return conn