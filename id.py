from bottle import route, run

@route("/<id:int>")
def id(id):
    if id == 1:
        return "Gunnar"
    elif id == 2:
        return "Daníel"
    elif id == 3:
        return "þórarinn"
    else:
        return "<h1>Ekkert fundið<br>404</h1>"

run(host='localhost', port=8080)