from flask import Flask
import sqlite3
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/create1')
def create():
    conn = sqlite3.connect('test.db')
    print ("Opened database successfully")

    conn.execute('''CREATE TABLE COMPANY
            (ID            INT     NOT NULL,
            NAME           TEXT    NOT NULL,
            AGE            INT     NOT NULL,
            ADDRESS        CHAR(50),
            SALARY         REAL);''')
    print ("Table created successfully")

    conn.close()

    return 'table created successfully'

@app.route('/insert')
def insert():
    conn = sqlite3.connect('test.db')
    print ("Opened database successfully")

    # conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #     VALUES (1, 'Paul', 32, 'California', 20000.00 )")

    conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES(?, ?, ?, ?, ?)", 
                    (str(random.seed(100)), 'Paul', 32, 'California', 20000.00))

    conn.commit()
    print ("Records created successfully")
    conn.close()

    return 'record inserted successfully'

@app.route('/select')
def select():
    name = ""
    conn = sqlite3.connect('test.db')
    print ("Opened database successfully")

    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3])
        name = row[1]

    print ("Operation done successfully")
    conn.close()

    return name

if __name__ == '__main__':
    app.run()
