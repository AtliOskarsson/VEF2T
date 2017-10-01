# Atli Óskarsson
# Verkefni 6

# Atli óskarsson
# Verkefni 5

from bottle import route, run, static_file, template, redirect, request

@route("/")
def yeh():
    return template("template/index.tpl")
@route("/send", method="POST")
def senda():
    upplysingar = {}
    nafn = request.forms.get("nafn")
    nafn = nafn.strip(" ")
    password = request.forms.get("password")
    notendanafn = request.forms.get("notendanafn")
    netfang = request.forms.get("email")
    simanumer = request.forms.get("simanumer")
    upplysingar.update({"nafn": nafn, "netfang": netfang, "simanumer": simanumer, "password": password, "notendanafn": notendanafn})

    if "@" not in netfang or "." not in netfang:
        upplysingar.update({"villa": "Email villa"})
        return template("template/villa.tpl", upplysingar)

    if len(password) < 5:
        upplysingar.update({"password": "", "villa": "Það verða að vera fleiri enn 5 stafir í lykilorðinu"})
        return template("template/villa.tpl", upplysingar)

    if " " in notendanafn:
        upplysingar.update({"villa": "Ekkert bil í notendanafni"})
        return template("template/villa.tpl", upplysingar)

    print(upplysingar)
    return template("template/upplysingar.tpl", upplysingar)

@route('/CSS/<filename>')
def server_static(filename):
    return static_file(filename, root="CSS")

run(host="localhost", port="8080", debug=True)