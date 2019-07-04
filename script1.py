import cherrypy 
import os 

class Samra(object): 
    
    @cherrypy.expose() 
    def index(self): 
        return """ 
            <form method="post" action="processform"> 
            Enter text:<input type="text" name="input"><br> 
            Language:<input type="text" name="lang"><br>
            <input type="submit"> 
            """ 
            #var input = document.getElementById("input").value
            #var lang = document.getElementById("lang").value

    @cherrypy.expose() 
    def processform(self, find): 
        os.system('python script2.py "%s"' % (find)) 
        return "Tranliterated output goes here." 


        
cherrypy.quickstart(Samra(), "/") 