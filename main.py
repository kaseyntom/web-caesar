from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>

        <style>
            form {{
                background-color: #eee;
                padding: 20 px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10 px;

            }}

            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;

            }}
            </style>
    
            <body>

    <form method='POST' />
        <label>Rotate by 
        <input type="text" name='rot' />
        </label>
      <textarea name="text">{0}</textarea> 
        <input type="submit" /> 
       </form>  
    </body>
</html>
      

"""
  
@app.route("/")
def index():

     return form.format("")

@app.route("/" , methods=['POST'])
def encrypt():

    rot = int(request.form['rot'])
    message = (request.form['text'])
    
    encrypted_message = rotate_string(message, rot)

    return  form.format(encrypted_message)

app.run()