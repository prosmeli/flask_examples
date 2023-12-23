from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/index/')
@app.route('/')
@app.route('/<name>')
def root(name = None):
    return render_template("index.html", my_name=name)

@app.route('/books/')
def books():
    with open("my_books.json") as json_file:
        my_data = json.load(json_file)
        print(my_data)

    return render_template("books.html", my_data = my_data)

if __name__ == "__main__":
    app.run(debug=True)