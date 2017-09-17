# Atli Óskarsson
# Verkefni 4.1

from bottle import route, run, static_file, template, error

@route("/")
def jobs():
    info = {"css": "CSS/styles.css", "title": "Steve Jobs", "link1": "/bio", "link2": "/pic", "linktext1": "Biography", "linktext2": "Pictures", "contact": "5530987", "mynd1": "myndir/steve_jobs.png", "text":"Steve Jobs was born in San Francisco, California, on February 24, 1955, to two University of Wisconsin graduate students who gave him up for adoption. Smart but directionless, Jobs experimented with different pursuits before starting Apple Computer with Steve Wozniak in 1976. Apple's revolutionary products, which include the iPod, iPhone and iPad, are now seen as dictating the world."}
    return template("template/index1.tpl", info)

@route("/bio")
def bio():
    info = {"css": "CSS/styles.css", "title": "Biography", "link1": "/", "link2": "/pic", "linktext1": "Steve Jobs", "linktext2": "Pictures", "contact": "8474653", "mynd1": "myndir/steve_jobs.png", "text": "Steve Jobs was born in San Francisco, California, on February 24, 1955, to two University of Wisconsin graduate students who gave him up for adoption. Smart but directionless, Jobs experimented with different pursuits before starting Apple Computer with Steve Wozniak in 1976. Apple's revolutionary products, which include the iPod, iPhone and iPad, are now seen as dictating the evolution of modern technology, with Jobs having left the company in 1985 and returning more than a decade later. He died in 2011, following a long battle with pancreatic cancer."}
    return template("template/index1.tpl", info)

@route("/pic")
def bio():
    info = {"css": "CSS/styles.css", "title": "Pictures", "link1": "/", "link2": "/bio", "linktext1": "Steve Jobs", "linktext2": "Biography", "contact": "8217202", "mynd1": "myndir/first_iphone.png", "mynd2": "myndir/steve_jobs.png", "mynd3": "myndir/iphone_x.png"}
    return template("template/index2.tpl", info)

@error(404)
def error404(error):
    info = {"css": "CSS/styles.css", "title": "404 Not Found", "link1": "/", "link2": "/bio", "link3": "/pic", "linktext1": "Steve Jobs", "linktext2": "Biography", "linktext3": "Pictures", "contact": "654968469", "gif": "myndir/notfound.gif"}
    return template("template/indexerror.tpl", info)

@route('/CSS/<filename>')
def server_static(filename):
    return static_file(filename, root="CSS")

@route('/myndir/<filename:re:.*\.png>')
def server_static(filename):
    return static_file(filename, root="myndir", mimetype=".png")

@route('/myndir/<filename:re:.*\.gif>')
def server_static(filename):
    return static_file(filename, root="myndir", mimetype=".gif")

if __name__ == "__main__":
    run(debug=True)