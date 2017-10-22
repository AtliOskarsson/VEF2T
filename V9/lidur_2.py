# Atli Óskarsson
from bottle import *
import urllib.request, json

with urllib.request.urlopen("http://apis.is/currency/arion") as url:
    data = json.loads(url.read().decode())
print(data)
for i in data['results']:
    print("Nafn :", i)
@route('/')
def index():
    return template("template/lidur_2.tpl", posts=data)

@route('/CSS/<filename>')
def server_static(filename):
    return static_file(filename, root="CSS")

run(host="localhost", port="8080", debug=True)