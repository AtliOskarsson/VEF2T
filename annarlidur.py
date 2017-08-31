from bottle import route, run

@route("/hello/02")
def hello():
    return "<b>Halló Heimur!</b>"

run(host='localhost', port=8080)