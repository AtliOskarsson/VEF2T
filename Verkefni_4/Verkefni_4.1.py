# Atli Óskarsson
# Verkefni 4.1

from bottle import route, run, static_file, template

info = {'numer': '123', 'gata': 'Fake St.', "borg": 'Fakeville'}
tpl = "I live at {{numer}} {{gata}}, {{borg}}"
@route("/")
def word():
    return template(tpl, info)

@route('/CSS/<filename>')
def server_static(filename):
    return static_file(filename, root="CSS")

@route('/images/<filename:re:.*\.png>')
def server_static(filename):
    return static_file(filename, root="images", mimetype=".png")

if __name__ == "__main__":
    run(debug=True)
