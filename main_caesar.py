from flask import Flask, request
from webcaesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            <label for="rot">Rotate by:
            <input type="text" id="rot" name="rot" value="0" />
            </label>
            <br>
            <label for="text">
            <textarea id="text" name="text" value=''>{text}</textarea>
            </label>

            <input type="submit" value="Encode"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(text='')

@app.route("/", methods=['POST'])
def mask():
    shift_by = int(request.form['rot'])
    original_text = request.form['text']
    new_text = encrypt(original_text,shift_by)
    return form.format(text=new_text)

app.run()