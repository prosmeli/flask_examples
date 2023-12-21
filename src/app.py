from flask import Flask

app = Flask(__name__)

@app.route('/index/')
@app.route('/')
def root():
    return """
    <html>

    <head>
        <title>This is my first web page</title>
    </head>

    <body>
        <h1>Hello World!</h1>
        <p>This is a simple paragraph.</p>
        <p>This is a second paragraph.</p>
    </body>

    </html>
    """

@app.route('/hello/')
def hello():
    return "Hello"

@app.route('/hello2/<name>')
def hello2(name):
    return f"Hello {name}!"

@app.route('/hello3/<int:id>')
def hello3(id):
    return f"My id is: {id}!"

if __name__ == "__main__":
    app.run(debug=True) # False when our app has been uploaded to production server.