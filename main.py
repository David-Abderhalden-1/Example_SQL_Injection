from flask import Flask, request, render_template, escape, session, redirect, url_for
from Example_SQL_Injection import mydata

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def sessions():

    if request.method == 'POST':
        session['name'] = request.form['username']
        session['password'] = request.form['password']
        if mydata.login_checker(session['name'], session['password']):
            if not session['name'] or not session['password'] == 0:
                return redirect(request.url)
        else:
            return render_template("index.html")
    else:
        if 'name' in session:
            return render_template("login.html", name=escape(session['name']))
        else:
            return render_template("index.html")


app.secret_key = "b'\xba\x9d\xa4oBU\x8d/\x96\xe1\x04\x0e\xb3\xc6\xd5\xca\x88\r$\x10\xa3\xf2i\x9a'"


@app.route("/logout", methods=['POST', 'GET'])
def logout():
    session.pop('name', None)
    return redirect(url_for('sessions'))


if __name__ == '__main__':
    app.run(port=1337, debug=True)
