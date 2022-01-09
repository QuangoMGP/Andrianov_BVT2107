import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="1304",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

back = True

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')
            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
            records = list(cursor.fetchall())
            try:
                return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])
            except IndexError:
                return render_template('error.html')
        elif request.form.get("registration"):
            return redirect("/registration/")
        else:
            render_template('login.html')

    return render_template('login.html')


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        if request.form.get("reg"):
            name = request.form.get('name')
            login = request.form.get('login')
            password = request.form.get('password')
            if login != "" and password != "":
                cursor.execute(f"SELECT * FROM service.users WHERE login='{login}'")
                records = list(cursor.fetchall())
                print(records)
                if records == []:
                    cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',
                                   (str(name), str(login), str(password)))
                    conn.commit()
                    return redirect('/login/')
                else:
                    return render_template('ex_error.html')
            else:
                return render_template('reg_error.html')
        elif request.form.get("back"):
            render_template('registration.html')

    return render_template('registration.html')


