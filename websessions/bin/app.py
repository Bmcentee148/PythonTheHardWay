"""An example of how to use user sessions in the python web framework."""

import web

urls = (
    '/', 'Index',
    '/login', 'Login',
    '/logout', 'Logout'
)

# Turn off web debugging so that user sessions work properly
web.config.debug = False 
app = web.application(urls, globals())
render = web.template.render('templates/')

# Create session that will be stored on disk in a directory named /sessions
session = web.session.Session(app, web.session.DiskStore('sessions'))

# Class for handling requests to '/' URL
class Index(object) :

    def GET(self) :
        if session.get('logged_in', False) :
            return render.logged_in()
        else :
            return render.logged_out()

# Class for handling requests to '/login' URL
class Login(object) :
    
    def GET(self) :
        session.logged_in = True
        raise web.seeother('/')


# Class for handling requests to '/logout' URL
class Logout(object) :
    
    def GET(self) :
        session.logged_in = False
        raise web.seeother('/')

if __name__ == '__main__' :
    app.run()