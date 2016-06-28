import web
import os

#map of urls to handler classes
urls = (
    '/hello', 'Index',  
    '/textUpload', 'TextUpload',
    '/imgUpload', 'ImgUpload'
)

#recognized img file extensions
IMG_FILE_EXTENSIONS = [
    '.img', '.png', '.jpg', '.gif'
]

#constant for path where uploaded files should be saved
UPLOAD_PATH = 'static/uploaded/'


app = web.application(urls, globals())
render = web.template.render('templates/', base="layout")

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

class TextUpload(object) :

    def GET(self) :
        # return the upload form when receiving a GET request
        return render.upload_text_form()

    def POST(self) :
        """Save the uploaded file in an appropriate folder."""
        
        #piece together saved files path and name
        upload = web.input(upload_file = {})
        f_name = upload.upload_file.filename

        if f_name[-4:] == ".txt" :
            fout_path = UPLOAD_PATH + f_name

            #copy uploaded files contents to appropriate file
            with open(fout_path, 'w') as fout :
                fout.write(upload.upload_file.file.read())
            return render.upload_text_conf(file_name = f_name)
        else :
            web.debug("Error: Expected a text file upload")

class ImgUpload(object) :

    def GET(self) :
        return render.upload_img_form()

    def POST(self) :
        upload = web.input(upload_file = {})
        file_name = upload.upload_file.filename
        if file_name[-4:].lower() in IMG_FILE_EXTENSIONS :
            fout_path = UPLOAD_PATH + file_name
            file_contents = upload.upload_file.file.read()
            with open(fout_path, 'w') as fout :
                fout.write(file_contents)
        else : 
            web.debug("Error: Expected and img file extension.")
        return render.upload_img_conf(file_name = file_name)


if __name__ == '__main__' :
    app.run()