import cherrypy

class Input(object): 
    
    @cherrypy.expose() 
    def index(self):
    	inp = ''
    	return """
    		<form action="input">
	    		<input id="inp" name="inp"></input>
	    		<input type="submit">
    		</form>
    		<script>
    			var x = document.getElementbyId('#inp');
    			%(inp)s = x;
    			"""%{"inp": inp}

    @cherrypy.expose()
    def input(self, inp):
    	return inp

    def getinp(self):
    	return self.inp

inpu = Input()

cherrypy.quickstart(inpu,'/')
print(inpu.getinp())

get = Input()
get.input()