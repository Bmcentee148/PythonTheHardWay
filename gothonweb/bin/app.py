#-- Import Statements --#
import web

#-- Main Script --#

# We can add multiple urls in a single tuple following the path, class pattern
urls = (
    '/' ,'index',
    '/hello', 'hello'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self) :
        result = 'Brian'
        return render.index(name = result) 

class hello: 
    def GET(self) :
        greeting = 'Hello, World!'
        return render.hello(greeting = greeting)

if __name__ == '__main__' :
    app.run()