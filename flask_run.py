from flask import Flask

app = Flask(__name__)

def _transliterate(inp, lang):
        #s = '' 
        print(inp)
        #os.system('python script2.py "%s"' % (find)) 
        #for i in inp:
        #   s = s + i
        ret = ''
        out_string = ''
        list_opt = ''
        out_opt = ''
        #words = inp.split(' ')
        inp = inp.replace('\n',' ').replace('\r', '')
        words = re.split(' ', inp)
        for word in words:
            #ret = ret + start.quillCherry.processWordJSON(word,lang) + ' '
        #if out == 'json':
            #return ret
        #elif out == 'text':
            print(word)
            ret = json.loads(start.quillCherry.processWordJSON(word, lang))
            #return """
            #<script>

               # var obj = JSON.parse(ret)          #Parsing through JavaScript
                #document.write(obj)
           # </script>

                   # """
            #return ret["twords"].options
            
            out_string = out_string + ret['itrans'] + ' '       #transliterating multiple words
            print("best option:" + out_string)
            
            opt = ret['twords'][0]['options']   #list of all options
            print("all options:")
            for item in opt:
            #    list_opt = list_opt + item + ' '
                print(item)
            
            
            #print(list_opt)
            #out_opt = out_opt + list_opt + ' '
        return out_string

@app.route('/')
def home():
	return """
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">

            <div class = "container">
                <h1><center>Matra</center></h1>
                <h5><center>an indic phonetic typing tool</center></h5>
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


                <div class="form-group">
                    <input type="submit" value="Transliterate" class="btn btn-info"> 
                </div>
                </form>
            </div>
            """

@app.route('/transliterate', methods=['GET', 'POST'])   #URL for website
def transliterate(inp, lang):
	return _transliterate(inp, lang) 
 	

if __name__ == "__main__":
	app.run(debug = True)