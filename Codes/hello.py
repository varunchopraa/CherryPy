import cherrypy
    	  
class HelloWorld(object):
    def index(self):
            return "Hello World!"
    index.exposed = True
  
     
cherrypy._cpconfig.Config('hello.conf')     
cherrypy.quickstart(HelloWorld())