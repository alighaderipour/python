# customer details
from database import *
class customer:
    def __init__(self,username, password, name, age, city, account_number):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__age = age
        self.__city = city
        self.__account_number = account_number

    def create_user(self):
        temp = db_query(f"insert into customers(username,password,name,age,city,account_number, status) values ('{self.__username}', "
                        f"'{self.__password}',"
                        f"'{self.__age}','{self.__age}','{self.__city}','{self.__account_number}', 1)")
        mydb.commit()