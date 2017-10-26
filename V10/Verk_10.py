from bottle import *
import pymysql.cursors

from bottle import *
from pymysql import *

db=Connect(host="tsuts.tskoli.is", user="0202002190", password="H2csgo1500", db="0202002190_vef2v10")
cursor=db.cursor()
cursor.execute("select * from user")

numrows=int(cursor.rowcount)


for i in range(numrows):
    row=cursor.fetchone()
    if row:
        print(row[0]), print(row[1]),

cursor.execute("insert into user(user,pass) values('bjarki','neiman')")
db.commit()
cursor.close()

@route("/")
def site():
    return("yes")

run(host="localhost", port="8080", debug=True)