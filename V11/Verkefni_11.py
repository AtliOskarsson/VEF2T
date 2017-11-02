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

for x in bilar_listi:
    if x["skraningarnumer"] == "AB-123":
        for i in x:
            print(x[i])


@route("/")
def search():
    skra = {}
    return template("template/search.tpl")

@route("/check", method="POST")
def check():
    skraning = request.forms.get("search")
    print(skraning)
    for x in bilar_listi:
        if x["skraningarnumer"] == skraning:
            for i in x:
                skra[i] = [x[i]]
            print(skra)
            return redirect("/result")
    return redirect("/")

@route("/result")
def result():
    return template("template/result.tpl", posts=bilar_listi)

@route("/edit")
def bilar():
    return template("template/index.tpl", posts=bilar_listi)



run(host="localhost", port="8080", debug=True)