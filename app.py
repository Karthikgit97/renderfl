from flask import Flask, render_template, request, url_for, flash, redirect
import datetime
import sqlite3

app = Flask(__name__)

db = 'selva.db'

@app.route('/')
def home():
    return redirect("https://deciduo.vercel.app", code=302)

@app.route('/create_db')
def create():
    conn = sqlite3.connect(db)
    print ("Opened database successfully")

    conn.execute('''CREATE TABLE data
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            TIMESTAMP      TEXT    NOT NULL,
            VALUE_1        INT     NOT NULL,
            VALUE_2        INT     NOT NULL,
            VALUE_3        INT     NOT NULL,
            VALUE_4        INT     NOT NULL,
            VALUE_5        INT     NOT NULL,
            VALUE_6        INT     NOT NULL);''')
    conn.close()

    print ("Table created successfully")
    return 'table created successfully'

@app.route('/insert', methods=['GET'])
def insert():
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    value3 = request.args.get('value3')
    value4 = request.args.get('value4')
    value5 = request.args.get('value5')
    value6 = request.args.get('value6')
    print(value1, value2, value3, value4, value6)
    print(str(datetime.datetime.now()))

    conn = sqlite3.connect(db)
    print ("Opened database successfully")

    # conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #     VALUES (1, 'Paul', 32, 'California', 20000.00 )")

    conn.execute("INSERT INTO data (TIMESTAMP, VALUE_1, VALUE_2, VALUE_3, VALUE_4, VALUE_5, VALUE_6) VALUES(?, ?, ?, ?, ?, ?, ?)", 
                    (str(datetime.datetime.now()), value1, value2, value3, value4, value5, value6))

    conn.commit()
    print ("Records created successfully")
    conn.close()

    return 'record inserted successfully'

@app.route('/view')
def select():
    name = "12"
    conn = sqlite3.connect(db)
    print ("Opened database successfully")

    cursor = conn.execute("SELECT * from data")
    results = cursor.fetchall()
    conn.close()

    print ("Operation done successfully")
    conn.close()

    return render_template("view.html", data=results)

if __name__ == '__main__':
    app.run()
