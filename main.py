from flask import Flask, request, render_template, escape, session, redirect, url_for
from Example_SQL_Injection import mydata

app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
def login():
    if 'name' in session:
        table = (mydata.list_converter())
        return render_template("index.html", name=escape(session['name']), password=escape(session['password']), table=table)
    else:
        return render_template("login.html")


app.secret_key = "b'\xba\x9d\xa4oBU\x8d/\x96\xe1\x04\x0e\xb3\xc6\xd5\xca\x88\r$\x10\xa3\xf2i\x9a'"


@app.route("/login", methods=['POST', 'GET'])
def sessions():
    if request.method == 'POST':
        if mydata.login_checker_injectable(request.form['username'], request.form['password']):
            if not request.form['username'] or not request.form['password'] == 0:
                session['name'] = request.form['username']
                session['password'] = request.form['password']
                return redirect(url_for('login'))
        else:
            return redirect(url_for('login'))


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        # check if data already exists.
        if not request.form['username'] or not request.form['password'] == 0:
            if not mydata.login_checker_safe(request.form['username'], request.form['password']):
                session['name'] = request.form['username']
                session['password'] = request.form['password']
                mydata.register(escape(session['name']), escape(session['password']))
                return redirect(url_for('login'))
            else:
                return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


@app.route("/logout", methods=['POST', 'GET'])
def logout():
    session.pop('name', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(port=1337, debug=True)
