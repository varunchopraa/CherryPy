import cherrypy

class trial(object):

	@cherrypy.expose
	def index(self):
		htm = '<!DOCTYPE html><head><script src=d></head><body><h1 id="hello">Hello</h1></body></html>'
		d = 'document.getElementbyId("hello").innerHTML = "Goodbye";'
		return htm, d

cherrypy.quickstart(trial(),"/")