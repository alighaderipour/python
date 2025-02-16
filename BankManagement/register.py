# user registeration signin and signup
from database import *
import random
from customer import *


def SignUP():
    username = input("create username: ")
    temp = db_query(f"select username from customers where username ='{username}';")
    if temp:
        print('Username Already Exists')
    else:
        print('Username Available Please Proceed')
        password = input('please choose a password: ')
        name = input('please choose a name: ')
        age = input('please choose a age: ')
        city = input('please choose a city: ')
        while True:
            account_number = random.randint(10000000, 99999999)
            temp = db_query(f"select account_number from customers where account_number = '{account_number}'")
            if temp:
                continue
            else:
                print(account_number)
                break
    cobj = customer(username=username, password=password, name=name, account_number=account_number, age=age, city= city)
    cobj.create_user()

def SignIn():
    pass
