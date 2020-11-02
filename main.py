from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return '''
        <html>
            <body>
                <form action="http://localhost:1337/login" method="post">
                    <p>Username:</p>
                    <p><input type="text" name="username"/></p>
                    <p><input type="submit" value="Send"/></p>
                </form>
            </body>
        </html>
    '''


@app.route('/login', methods=['POST', 'GET'])
def login():
    name = ""
    if request.method =='POST':
        name = request.form['username']
    else:
        name = request.args.get('username')
    return "Hallo " + name + "."


if __name__ == '__main__':
    app.run(port=1337, debug=True)