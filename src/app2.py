from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index/')
@app.route('/')
@app.route('/<name>')
def root(name = None):
    if name == None:
        return "Hello Guest"
    else:
        return render_template("index.html", my_name=name)

if __name__ == "__main__":
    app.run(debug=True)