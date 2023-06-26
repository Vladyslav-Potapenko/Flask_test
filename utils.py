import requests
import sqlite3
from faker import Faker


r = requests.get('http://api.open-notify.org/astros.json')
r.json()



def open_file():
     file = open('requirements.txt', 'r')
     result = file.read()
     file.close()
     return result

def random_users(length: int = 100) -> str:
    fake = Faker()
    fake.name()
    user_list = ' '
    for _ in range(length):
        user_list += '[' + fake.first_name() + ' - ' + fake.ascii_email() + ']' + ';\n'
    return user_list

def astronauts():
    astronauts = str(r.json()["number"])
    astronauts_in_space = ' '
    astronauts_in_space += ('Now in space' + ' ' + astronauts + ' ' + 'astronauts!')
    return astronauts_in_space

def commit_sql_email(sql):
    con = sqlite3.connect("example.db")
    cur = con.cursor()
    cur.execute(sql)

    con.commit()

    con.close()

def commit_sql_phone(sql):
    con = sqlite3.connect("phone.db")
    cur = con.cursor()
    cur.execute(sql)

    con.commit()

    con.close()

