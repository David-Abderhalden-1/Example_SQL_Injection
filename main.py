from flask import Flask, request, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    name = ""
    if request.method =='POST':
        name = request.form['username']
    else:
        name = request.args.get('username')
    return render_template("index.html", name=name)


if __name__ == '__main__':
    app.run(port=1337, debug=True)