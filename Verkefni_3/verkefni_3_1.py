# Atli Óskarsson
#Verkefni 3 - Liður 1

from bottle import route, run, static_file

@route("/<word>")
def word(word):
    if word == "jobs":
        return '''
                <!DOCTYPE html>
                <html>
                    <head>
                            <title>Steve Jobs</title>
                            <meta charset="utf-8">
                            <link type="text/css" rel="stylesheet" href="CSS/styles.css">
                    </head>
                    <body>
                        <a href="bio">Biography</a>
                        <a href="pictures">Pictures</a>
                        <h1>Steve Jobs</h1>
                        <p>Steve Jobs was born in San Francisco, California, on February 24, 1955, to two University of Wisconsin graduate students who
                        gave him up for adoption. Smart but directionless, Jobs experimented with different pursuits before starting Apple Computer with
                        Steve Wozniak in 1976. Apple's revolutionary products, which include the iPod, iPhone and iPad, are now seen as dictating the
                        evolution of modern technology, with Jobs having left the company in 1985 and returning more than a decade later. He died in 2011,
                        following a long battle with pancreatic cancer.</p>
                        <img src="images/steve_jobs.png">
                    </body>
                </html>
                '''
    elif word == "bio":
        return '''
                <!DOCTYPE html>
                <html>
                    <head>
                            <title>Biography</title>
                            <meta charset="utf-8">
                            <link type="text/css" rel="stylesheet" href="CSS/styles.css">
                    </head>
                    <body>
                        <a href="jobs">Steve Jobs</a>
                        <a href="pictures">Pictures</a>
                        <img src="images/biopic.png">
                        <p>Steve Jobs was born in San Francisco, California, on February 24, 1955, to two University of Wisconsin graduate students who
                        gave him up for adoption. Smart but directionless, Jobs experimented with different pursuits before starting Apple Computer with
                        Steve Wozniak in 1976. Apple's revolutionary products, which include the iPod, iPhone and iPad, are now seen as dictating the
                        evolution of modern technology, with Jobs having left the company in 1985 and returning more than a decade later. He died in 2011,
                        following a long battle with pancreatic cancer.</p>
                    </body>
                </html>
                '''
    elif word == "pictures":
        return '''
                <!DOCTYPE html>
                <html>
                    <head>
                            <title>Biography</title>
                            <meta charset="utf-8">
                            <link type="text/css" rel="stylesheet" href="CSS/styles.css">
                    </head>
                    <body>
                        <a href="jobs">Steve Jobs</a>
                        <a href="bio">Biography</a>
                        <h1>Pictures</h1>
                        <p>Steve Jobs was born in San Francisco, California, on February 24, 1955, to two University of Wisconsin graduate students who
                        gave him up for adoption. Smart but directionless, Jobs experimented with different pursuits before starting Apple Computer with
                        Steve Wozniak in 1976. Apple's revolutionary products, which include the iPod, iPhone and iPad, are now seen as dictating the
                        evolution of modern technology, with Jobs having left the company in 1985 and returning more than a decade later. He died in 2011,
                        following a long battle with pancreatic cancer.</p>
                        <img src="images/steve_jobs.png">
                    </body>
                </html>
                '''

@route('/CSS/<filename>')
def server_static(filename):
    return static_file(filename, root="CSS")

@route('/images/<filename:re:.*\.png>')
def server_static(filename):
    return static_file(filename, root="images", mimetype=".png")

run(host='localhost', port=8080)
