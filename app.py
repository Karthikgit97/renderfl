from flask import Flask, render_template, request, url_for, flash, redirect
import mysql.connector

mydb = mysql.connector.connect(
  host="sql12.freesqldatabase.com",
  user="sql12592719",
  password="HJugkzhjpl",
  database="sql12592719"
)

app = Flask(__name__)

@app.route('/')
def home():
    mycursor = mydb.cursor()

    #mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

    mycursor.execute("SHOW TABLES")
    qw = ""
    for x in mycursor:
        print(x)
        qw = str(x)
    
    return str(qw)

if __name__ == '__main__':
    app.run()
