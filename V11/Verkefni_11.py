from re import *
from bottle import *
from pymysql import *

db=Connect(host="tsuts.tskoli.is", user="0202002190", password="H2csgo1500", db="0202002190_vef2verk11")
cursor=db.cursor()
cursor.execute("select * from bilar")
numrows=int(cursor.rowcount)

bilar_listi = []

for i in range(numrows):
    row=cursor.fetchone()
    if row:
        bilar = {}
        bilar["skraningarnumer"] = row[0]
        bilar["tegund"] = row[1]
        bilar["verksmidjunumer"] = row[2]
        bilar["skraningadagur"] = row[3]
        bilar["co2"] = row[4]
        bilar["þyngd"] = row[5]
        bilar["skodun"] = row[6]
        bilar["stada"] = row[7]
        bilar_listi.append(bilar)

print(bilar_listi)
skra = {}


@route("/")
def search():
    cursor = db.cursor()
    cursor.execute("select * from bilar")
    numrows = int(cursor.rowcount)

    bilar_listi = []

    for i in range(numrows):
        row = cursor.fetchone()
        if row:
            bilar = {}
            bilar["skraningarnumer"] = row[0]
            bilar["tegund"] = row[1]
            bilar["verksmidjunumer"] = row[2]
            bilar["skraningadagur"] = row[3]
            bilar["co2"] = row[4]
            bilar["þyngd"] = row[5]
            bilar["skodun"] = row[6]
            bilar["stada"] = row[7]
            bilar_listi.append(bilar)
    return template("template/search.tpl")

@route("/check", method="POST")
def check():
    global skraning
    skraning = request.forms.get("search")
    print(skraning)
    for x in bilar_listi:
        if x["skraningarnumer"] == skraning:
            global skra
            for i in x:
                skra[i] = x[i]
            return redirect("/result")
    return redirect("/")

@route("/result")
def result():
    print(skra)
    return template("template/result.tpl", skra)

@route("/edit")
def bilar():
    return template("template/index.tpl")

@route("/eyda", method="POST")
def eyda():
    for x in skra:
        if x[2] == "-":
            val = x
    print(val)
    delete = "delete from bilar where skraningarnumer ='" + val + "';"
    print(delete)
    cursor.execute(delete)
    db.commit()
    cursor.close()
    redirect("/")


db.commit()
cursor.close()

@route('/CSS/<filename>')
def server_static(filename):
    return static_file(filename, root="CSS")

run(host="localhost", port="8080", debug=True)