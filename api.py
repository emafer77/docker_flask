from flask import Flask 
app = Flask(__name__)

@app.route('/pagina')
def hello_world():
    return "Hello worldyi!"
