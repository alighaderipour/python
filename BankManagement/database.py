# Database Management Banking
import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    password="Aa@123456",
    database="bank"
)

cursor = mydb.cursor()


def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result


def create_customer_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers
    (username varchar(20),
    password varchar(20),
    name varchar(20),
    age integer,
    city varchar(20),
    account_number integer,
    status boolean
    )
    ''')


mydb.commit()

if mydb.is_connected():
    print("Successfully connected to the database.")
else:
    print("Failed to connect to the database.")


create_customer_table()

