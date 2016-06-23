import web

#map of urls to handler classes
urls = (
    '/', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

# Handler class for the index page
class Index(object) :

    #Handler method for a GET request
    def GET(self) :
        greeting = 'Hello, World!'
        return render.Index(greeting = greeting)

if __name__ == '__main__' :
    app.run()