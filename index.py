from bottle import route, run

@route("/hello")
def hello():
    return "Halló Heimur!"

run(host='localhost', port=8080)