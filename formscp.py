import cherrypy
from pprint import pformat


class Root(object):
    """A default class for cherrypy that prints the request env.
    """

    @cherrypy.expose
    def index(self, *args, **kw):
        """We'll print the args and kw as well to show how arguments
        are passed to the dispatched method.
        
        Arguments:
        - `*args`: path args
        - `**kw`: query string / post variables
        """
        return '''
        <html><head><title>CP Info</title></head>
        <body><pre>%s</pre></body></html>
        ''' % pformat({
            'args': args,
            'kw': kw,
            'request': dict([(k, getattr(cherrypy.request, k))
                             for k in dir(cherrypy.request)
                             if not k.startswith('_')]),
        })

    @cherrypy.expose
    def forms(self, *args, **kw):
        return '''
<html>
<head>
<title>test forms</title>
</head>
<body>
<div>
%s
</div>
<form action="/forms" method="POST">
<input type="text" name="foo[]" value="x" /><br />
<input type="text" name="foo[]" value="y" /><br />
<input type="text" name="foo[]" value="z" /><br />
<input type="submit" name="submit" value="go" />
</form>
</body>
</html>
''' % pformat(kw)


if __name__ == '__main__':
    cherrypy.tree.mount(Root(), '/')
    cherrypy.engine.start()
    cherrypy.engine.block()