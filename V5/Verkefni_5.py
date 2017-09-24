# Atli óskarsson
# Verkefni 5

from bottle import route, run, static_file, template, redirect, request

@route("/")
def yeh():
    return template("template/index.tpl")
@route("/send", method="POST")
def senda():
    steard = request.forms.get("steard")
    return steard

run(host="localhost", port="8080", debug=True)