from bottle import route, run

@route("/<id:str>")
def id(id):
    if id == "steve-jobs":
        return "<ul><li><a href='http://localhost:8080/steve-Jobs'>Steve Jobs</a></li><li><a href='http://localhost:8080/biography'>Biography</a></li><li><a href='http://localhost:8080/pictures'>Pictures</a></li></ul>"
    elif id == "biography":
        return '<ul><li><a href="http://localhost:8080/steve-Jobs">Steve Jobs</a></li><li><a href="http://localhost:8080/biography">Biography</a></li><li><a href="http://localhost:8080/pictures">Pictures</a></li></ul>'
    elif id == 3:
        return '<ul><li><a href="http://localhost:8080/steve-Jobs">Steve Jobs</a></li><li><a href="http://localhost:8080/biography">Biography</a></li><li><a href="http://localhost:8080/pictures">Pictures</a></li></ul>'
    else:
        return "<h1>Ekkert fundið<br>404</h1>"

run(host='localhost', port=8080)