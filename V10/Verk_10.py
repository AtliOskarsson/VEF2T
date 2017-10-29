from bottle import *
from pymysql import *

db=Connect(host="tsuts.tskoli.is", user="0202002190", password="H2csgo1500", db="0202002190_vef2v10")
cursor=db.cursor()
cursor.execute("select * from user")
numrows=int(cursor.rowcount)

users = []
passwords = []

for i in range(numrows):
    row=cursor.fetchone()
    if row:
        print(row[0]), print(row[1])
        users.append(row[0])
        passwords.append(row[1])
print(users)
print(passwords)

@route("/")
def login():
    return template("template/index.tpl")

@route("/check", method="POST")
def check():
    notendanafn = request.forms.get("notendanafn")
    notenda_password = request.forms.get("password")
    svar = ""
    for x in range(len(users)):
        if users[x] == notendanafn:
            svar = passwords[x]

    if notendanafn in users and svar == notenda_password or request.get_cookie("visited"):
        response.set_cookie("visited", "yes")
        return redirect("/admin")
    else:
        return redirect("/")

@route("/signup", method="POST")
def check():
    notendanafn = request.forms.get("notendanafn")
    notenda_password = request.forms.get("password")
    if notendanafn not in users:
        response.set_cookie("visited", "yes")
        strengur = str("insert into user(user,pass) values('"+notendanafn+"','"+notenda_password+"')")
        print(strengur)
        cursor.execute(strengur)
        return redirect("/admin")
    else:
        return redirect("/")

@route("/admin")
def admin():
    if request.get_cookie("visited"):
        return template("template/admin.tpl")
    else:
        return redirect("/")

@route("/logout", method="POST")
def logout():
    response.set_cookie("visited", "", expires=0)
    return redirect("/")

db.commit()
cursor.close()

@route('/CSS/<filename>')
def server_static(filename):
    return static_file(filename, root="CSS")

run(host="localhost", port="8080", debug=True)