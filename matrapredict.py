import startquill_cherry as start
import cherrypy
import json
import re

class Input(object): 
    
    @cherrypy.expose() 
    def index(self, inp, lang):
        return """
            <!doctype html>
            <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <title>jQuery UI Autocomplete - Default functionality</title>
                    <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
                    <link rel="stylesheet" href="/resources/demos/style.css">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
                    <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
                    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
            
                    <body>
                        <div class = "container">
                            <h1><center>Matra</center></h1>
                            <h5><center>An indic phonetic typing tool</center></h5>
                            <br><br>
           
                        <form method="post" action="transliterate" id="input"> 
            

                        <div class="form-group">
                            Select language:
                            <select class="form-control" name="lang">
                                <option value="bengali">Bengali</option>
                                <option value="gujarati">Gujarati</option>
                                <option value="hindi">Hindi</option>
                                <option value="eng">English</option>
                                <option value="kannada">Kannada</option>
                                <option value="malayalam">Malayalam</option>
                                <option value="marathi">Marathi</option>
                                <option value="nepali">Nepali</option>
                                <option value="punjabi">Punjabi</option>
                                <option value="tamil">Tamil</option>
                                <option value="telugu">Telugu</option>
                            </select>
                        </div>
                        <br>

                        <div class="form-group">
                            Enter text: <br>
                            <textarea name="inp" form="input" rows="5" class="form-control"></textarea>
                        </div>
                        <br> 

                        <!--
                        <div class="form-group">
                            Output type:
                            <select class="form-control" name="out">
                                <option value="json">JSON Object</option>
                                <option value="text">Text</option>
                            </select>
                        </div><br>
                        -->

                        <script>
                            $( function() {
                              var availableTags = %(Xlit)s;                             #####Add options here somehow
                              $( "#inp" ).autocomplete({
                                source: availableTags
                              });
                            } );
                        </script>

                        <div class="form-group">
                            <input type="submit" value="Transliterate" class="btn btn-info"> 
                        </div>
                        </form>
                    </div>
                """% {"Xlit": self.transliterate(inp, lang)}
               
    #@cherrypy.expose() 
    def transliterate(self, inp, lang):
        #s = '' 
        #print(inp)
        #os.system('python script2.py "%s"' % (find)) 
        #for i in inp:
        #   s = s + i
        ret = ''
        out_string = ''
        list_opt = ''
        out_opt = ''
        #words = inp.split(' ')
        words = re.split(' '|'\n', inp)
        for word in words:
            print(word)
            ret = json.loads(start.quillCherry.processWordJSON(word, lang))
            
            out_string = out_string + ret['itrans'] + ' '       #transliterating multiple words
            print("best option:" + out_string)
            
            opt = ret['twords'][0]['options']                   #list of all options
            print("all options:")
            for item in opt:
            #    list_opt = list_opt + item + ' '
                print(item)
            
            
            #print(list_opt)
            #out_opt = out_opt + list_opt + ' '
        return opt
        '''    
        return """ 
        <head>
            <meta charset="utf-8">
            <script type="text/javascript">
                var out = %(out_string);
            </script>
        </head>

        <body>
            <script type="text/javascript">
                document.write(out);
            </script>
        </body>
        """
        '''

cherrypy.quickstart(Input(), "/") 

