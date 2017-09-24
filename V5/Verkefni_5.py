# Atli óskarsson
# Verkefni 5

from bottle import route, run, static_file, template, redirect, request

@route("/")
def yeh():
    return template("template/index.tpl")
@route("/send", method="POST")
def senda():
    upplysingar = {}
    pizzu_listi = {"9-tommu": 1000, "12-tommu": 1500, "15-tommu": 2000, "skinka": 200, "ananas": 200, "pepperoni": 200}
    nafn = request.forms.get("nafn")
    heimilisfang = request.forms.get("heimilisfang")
    netfang = request.forms.get("email")
    simanumer = request.forms.get("simanumer")
    staerd = request.forms.get("staerd")
    alegg = request.forms.get("alegg")
    utkoma = pizzu_listi.get(staerd) + pizzu_listi.get(alegg)
    virdiskattur = utkoma * 1.25
    virdiskattur = str(virdiskattur)
    upplysingar.update({"nafn": nafn, "heimilisfang": heimilisfang, "netfang": netfang, "simanumer": simanumer, "staerd": staerd, "alegg": alegg, "utkoma": utkoma, "verd_staerd": pizzu_listi.get(staerd), "verd_alegg": pizzu_listi.get(alegg), "virdisaukaskattur": virdiskattur})

    return template("template/upplysingar.tpl", upplysingar)

@route('/CSS/<filename>')
def server_static(filename):
    return static_file(filename, root="CSS")

run(host="localhost", port="8080", debug=True)