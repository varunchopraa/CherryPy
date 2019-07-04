import cherrypy
import json

class Input(object): 
    
    @cherrypy.expose() 
    def index(self):
    	#colors = ["red","green","blue","black","yellow"]
    	return """
    	<script src="jquery.easy-autocomplete.min.js"></script>
    	<link rel="stylesheet" href="easy-autocomplete.min.css">
    	<script
			  src="https://code.jquery.com/jquery-3.4.1.min.js">
		</script>
		<script>
    			var options = {
    				url: "colors.js";
    			};
    			$("#inp").easyAutocomplete(options);
    	</script>
    	
    		<input id="inp" />
    		
    			"""

cherrypy.quickstart(Input(), "/") 