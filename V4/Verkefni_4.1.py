# Atli Óskarsson
# Verkefni 4.1

from bottle import route, run, static_file, template, error

@route("/")
def jobs():
    info = {"css": "CSS/styles.css", "title": "Steve Jobs", "link1": "/bio", "link2": "/pic", "linktext1": "Biography", "linktext2": "Pictures", "contact": "5530987", "text":"Steve Jobs was born in San Francisco, California, on February 24, 1955, to two University of Wisconsin graduate students who gave him up for adoption. Smart but directionless, Jobs experimented with different pursuits before starting Apple Computer with Steve Wozniak in 1976. Apple's revolutionary products, which include the iPod, iPhone and iPad, are now seen as dictating the world."}
    return template("template/index1.tpl", info)

@route("/bio")
def bio():
    info = {"css": "CSS/styles.css", "title": "Biography", "link1": "/", "link2": "/pic", "linktext1": "Steve Jobs", "linktexti2": "Pictures", "contact": "8474653", "text": "Steve Jobs was born in San Francisco, California, on February 24, 1955, to two University of Wisconsin graduate students who gave him up for adoption. Smart but directionless, Jobs experimented with different pursuits before starting Apple Computer with Steve Wozniak in 1976. Apple's revolutionary products, which include the iPod, iPhone and iPad, are now seen as dictating the evolution of modern technology, with Jobs having left the company in 1985 and returning more than a decade later. He died in 2011, following a long battle with pancreatic cancer."}
    return template("index1.tpl", info)

@route("/pic")
def bio():
    info = {"css": "CSS/styles.css", "title": "Pictures", "link1": "/", "link2": "/bio", "linktexti1": "Steve Jobs", "linktexti2": "Biography", "contact": "8217202", "texti": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam finibus venenatis orci quis mattis. Curabitur facilisis elementum magna vitae semper. Morbi hendrerit, eros lacinia sollicitudin pharetra, erat metus lobortis est, id ultricies arcu lacus at neque. Sed mattis metus ante, eu pretium eros condimentum ac"}
    return template("index2.tpl", info)

@route('/CSS/<filename>')
def server_static(filename):
    return static_file(filename, root="CSS")

@route('/images/<filename:re:.*\.png>')
def server_static(filename):
    return static_file(filename, root="images", mimetype=".png")

if __name__ == "__main__":
    run(debug=True)