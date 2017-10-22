# Atli Óskarson
# Verkefni 9 - Liður 1
from bottle import *
import json
myndir = {'mynd1':'myndir/mynd1.png','mynd2':'myndir/mynd2.png', "mynd3": "myndir/mynd3.png"}
with open('photos.json', "w") as skra:
    json.dump(myndir, skra)

mynd_add = {"mynd4": "myndir/mynd4.png"}

with open("photos.json") as skra:
    gogn = json.load(skra)


gogn.update(mynd_add)

with open("photos.json", "w") as skra:
    json.dump(gogn, skra)
@route("/")
def mynd():
    return template("template/index.tpl", gogn)

@route('/myndir/<filename>')
def server_static(filename):
    return static_file(filename, root="myndir")

@route('/CSS/<filename>')
def server_static(filename):
    return static_file(filename, root="CSS")

run(host="localhost", port="8080", debug=True)