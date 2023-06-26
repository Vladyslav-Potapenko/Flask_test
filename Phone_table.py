import sqlite3


def create_table():
    con = sqlite3.connect('phone.db')
    cur = con.cursor()

    sql = '''
    CREATE TABLE Phones (
    PhoneId INTEGER PRIMARY KEY,
    ContactName varchar(255),
    PhoneValue varchar(255)
    )'''


    cur.execute(sql)

    con.commit()

    con.close()


if __name__ == '__main__':
    create_table()