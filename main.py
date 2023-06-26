import requests
import sqlite3
from flask import Flask, request
from utils import open_file, random_users, astronauts, commit_sql_email, commit_sql_phone

r = requests.get('http://api.open-notify.org/astros.json')
r.json()


app = Flask(__name__)

@app.route("/requirements")
def read_file():
    file_content = open_file()
    print(file_content)
    return open_file()

@app.route("/generate_users/")
def generate_users():
    length = request.args.get('length', '100')

    if length.isdigit():
        length = int(length)
    else:
        return f'Invalid value [ {length} ], you can only enter numbers from 1 to 200'

    if length > 200:
        return 'Length should be less than 200'

    return random_users(length)

@app.route("/space/")
def space():
    astronauts_in_space = astronauts()
    return astronauts_in_space



@app.route('/email/create')
def email_create():
    email = request.args['email']

    sql = f"""
    INSERT INTO Emails (EmailValue)
    VALUES ("{email}");
    """
    commit_sql_email(sql)

    return 'email_create'

@app.route("/email_read")
def email_read():
    ordering = request.args.get('ordering')
    con = sqlite3.connect("example.db")
    cur = con.cursor()

    if ordering:
        direction = 'DESC' if ordering.startswith('-') else 'ASC'
        field = ordering.strip('-')

        sql = f"""
            SELECT * FROM Emails ORDER BY {field} {direction};
            """
    else:
        sql = f"""
            SELECT * FROM Emails;
            """
    cur.execute(sql)

    result = cur.fetchall()

    con.close()

    return str(result)

@app.route("/email/update")
def email_update():
    email = request.args['email']
    email_id = request.args['email_id']

    sql = f"""
    UPDATE Emails
    SET EmailValue = '{email}'
    WHERE EmailId = {email_id};
    """
    commit_sql_email(sql)

    return 'Email_update'

@app.route("/email/delete")
def email_delete():
    email_id = request.args['email_id']

    sql = f"""
        DELETE FROM Emails 
        WHERE EmailId = {email_id};
        """
    commit_sql_email(sql)

    return 'Email_delete'

@app.route('/phone/create')
def phone_create():
    name = request.args['name']
    phone = request.args['phone']

    sql = f"""
    INSERT INTO Phones (ContactName, PhoneValue)
    VALUES ("{name}", {phone});
    """
    commit_sql_phone(sql)

    return 'Phone_create'

@app.route("/phone_read")
def phone_read():
    ordering = request.args.get('ordering')
    con = sqlite3.connect("phone.db")
    cur = con.cursor()

    if ordering:
        direction = 'DESC' if ordering.startswith('-') else 'ASC'
        field = ordering.strip('-')

        sql = f"""
            SELECT * FROM Phones ORDER BY {field} {direction};
            """
    else:
        sql = f"""
            SELECT * FROM Phones;
            """
    cur.execute(sql)

    result = cur.fetchall()

    con.close()

    return str(result)

@app.route("/phone/update")
def phone_update():
    name = request.args['name']
    phone = request.args['phone']
    phone_id = request.args['phone_id']

    sql = f"""
    UPDATE Phones
    SET Contactname = '{name}', PhoneValue = '{phone}'
    WHERE PhoneId = {phone_id};
    """
    commit_sql_phone(sql)

    return 'Phone_update'

@app.route("/phone/delete")
def phone_delete():
    phone_id = request.args['phone_id']

    sql = f"""
        DELETE FROM Phones 
        WHERE PhoneId = {phone_id};
        """
    commit_sql_phone(sql)

    return 'Phone_delete'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

print(a)