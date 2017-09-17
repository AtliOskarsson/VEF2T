# Atli Óskarsson
# Verkefni 4.2

from bottle import route, run, static_file, template, error

@route("/<id:int>")
def id(id):
    if id == 1:
        info = {"css": "CSS/styles.css", "title": "Pictures", "link1": "2", "link2": "3", "link3": "4", "linktext1": "Segist ekki hafa skrifað undir bréfið sem Hjalti Sigurjón skilaði í ráðuneytið", "linktext2": "Emmy verðlaunin veitt í kvöld", "linktexti3": "Viðbúnaðarstig lækkað í Bretlandi", "contact": "8217202", "mynd1": "myndir/ekki_skrifad.png", "mynd2": "myndir/emmy.png", "mynd3": "myndir/bretland_laekar_vidbunarstig.png"}
        return template("template/index.tpl", info)
    elif id == "2":
        info = {"css": "CSS/styles.css", "title": "Segist ekki hafa skrifað undir bréfið sem Hjalti Sigurjón skilaði í ráðuneytið", "link": "1", "linktext": "Forsíða", "contact": "Kolbeinn Tumi Daðason - kolbeinntumi@gmail.com", "mynd1": "myndir/steve_jobs.png", "text":"Hjalti Sigurjón Hauksson skilaði inn þremur umsögnum með umsókn sinni um uppreist æru í maí í fyrra. Fréttastofa hefur fengið umsókn Hjalta afhenta frá dómsmálaráðuneytinu ásamt umsögnum aðilanna þriggja. Er ýmislegt sem bendir til þess að átt hafi verið við umsagnarbréfin."}
        return template("template/index1.tpl", info)
    elif id == 3:
        info = {"css": "CSS/styles.css", "title": "Emmy verðlaunin veitt í kvöld", "link": "1", "linktext": "Forsíða", "contact": "Anton Egilsson - antonegils@gnail.com", "mynd1": "myndir/steve_jobs.png", "text": "Hin virtu Emmy verðlaun verða veitt í 69 skipti við hátíðlega athöfn í Microsoft Theater í Los Angeles í kvöld.  Kynnir kvöldsins verður grínistinn og spjallþáttastjórnandinn Stephen Colbert."}
        return template("template/index1.tpl", info)
    elif id == 4:
        info = {"css": "CSS/styles.css", "title": "Viðbúnaðarstig lækkað í Bretlandi", "link": "1", "linktext": "Forsíða", "contact": "Anton Egilsson - antonegils@gnail.com", "mynd1": "myndir/steve_jobs.png", "text": "Píratar munu líklega halda sameiginlegt prófkjör á höfuðborgasvæðinu líkt og fyrir síðustu kosning­ar en það er aðildarfélaganna að ákveða. Þetta segir Snæbjörn Brynjarsson, formaður framkvæmdaráðs Pírata."}
        return template("template/index1.tpl", info)

@error(404)
def error404(error):
    info = {"css": "CSS/styles.css", "title": "404 Not Found", "link": "1", "linktext": "Forsíða", "contact": ":(", "gif": "myndir/notfound.gif"}
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