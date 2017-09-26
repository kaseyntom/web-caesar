from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>

    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20 px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10 px;

            }

            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;

            }}
            </style>
        </head>
    <body>

    <form method='POST' />
        <label>Rotate by
        <input name="rot"  type='text' />
        </label>
      <textarea name="text">{0}</textarea> 
        <input type="submit"  /> 
       </form>
    </body>
</html>
      

"""
    
@app.route("/",  methods=['POST', "GET"])
def encrypt():


    rot_by = int(request.form['rot'])
    message = str(request.form['text'])
    
    encrypted_message = rotate_string(message, rot_by)

    return  form.format( """<h1>"""  + encrypted_message +   """</h1>""")


@app.route('/')
def index():

    return  form.format('') 
    
app.run()
    