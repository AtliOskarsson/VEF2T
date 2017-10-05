# Atli Óskarsson
# Verkefni 7

from bottle import route, run, static_file, template, redirect, request, response

@route("/")
def login():
    return template("template/index.tpl")

@route("/check", method="POST")
def check():
    notendanafn = request.forms.get("notendanafn")
    notenda_password = request.forms.get("password")
    if nafn == notendanafn and password == notenda_password or request.get_cookie("visited"):
        response.set_cookie("visited", "yes")
        return redirect("/admin")
    else:
        return redirect("/")
password = "admin"
nafn = "admin"


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



@route('/CSS/<filename>')
def server_static(filename):
    return static_file(filename, root="CSS")

run(host="localhost", port="8080", debug=True)