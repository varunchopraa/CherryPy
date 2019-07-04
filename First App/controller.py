#!/usr/bin/env python
import sys
import cherrypy
import os

class Root(object):

   def __init__(self, data):
      self.data = data

   @cherrypy.expose
   def index(self):
      tmpl = loader.load('index.html')
    
      return tmpl.generate(title='Sample').render('html', doctype='html')

   @cherrypy.expose
   def submit(self, cancel = False, **value):
   
      if cherrypy.request.method == 'POST':
         if cancel:
            raise cherrypy.HTTPRedirect('/') # to cancel the action
         link = Link(**value)
         self.data[link.id] = link
         raise cherrypy.HTTPRedirect('/')
      tmp = loader.load('submit.html')
      streamValue = tmp.generate()
      
      return streamValue.render('html', doctype='html')

def main(filename):
   data = {} # will be replaced with proper functionality later

   # configuration file
   cherrypy.config.update({
      'tools.encode.on': True, 'tools.encode.encoding': 'utf-8',
      'tools.decode.on': True,
      'tools.trailing_slash.on': True,
      'tools.staticdir.root': os.path.abspath(os.path.dirname(__file__)),
   })

   cherrypy.quickstart(Root(data), '/', {
      '/media': {
         'tools.staticdir.on': True,
         'tools.staticdir.dir': 'static'
      }
   })
	
if __name__ == '__main__':
   main(sys.argv[1])