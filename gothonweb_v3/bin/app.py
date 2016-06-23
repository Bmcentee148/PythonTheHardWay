import web

#map of urls to handler classes
urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

# Handler class for the index page
class Index(object) :

    #Handler method for a GET request
    def GET(self) :
        return render.hello_form()

    #Handler method for a POST request
    def POST(self) :
        form = web.input(greet = "Hello", name = "Nobody")
        greeting = "{0} {1}".format(form.greet, form.name)
        return render.index(greeting = greeting)

if __name__ == '__main__' :
    app.run()