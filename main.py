from flask import Flask, request, render_template, escape, redirect, url_for, send_from_directory
import mydata
import mydata_safe
import os

app = Flask(__name__)


# Main Route
@app.route('/index', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = (request.form['username'])
        password = (request.form['password'])
        if mydata.login_checker_injectable(username, password):
            return render_template('index.html', name=escape(username))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('login.html')


# Route to favicon
@app.route('/favicon.ico')
def fav():
    return send_from_directory(os.path.join(app.root_path, 'img'),'favicon.ico')

if __name__ == '__main__':
    app.run(port=1337, debug=True)
