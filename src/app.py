from flask import Flask, render_template, redirect, url_for, request
import json
from forms import SignupForm

app = Flask(__name__)

app.config["SECRET_KEY"] = 'c35a16d06a8c9289f5c7582a51d9b98b0cf1b4860566784380995246195a0989'

@app.route('/index/')
@app.route('/')
def root():
    return render_template("index.html")

@app.route('/signup/', methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        password2 = form.password2.data
        print(username, email, password, password2)
    return render_template("signup.html", form=form)

@app.route('/login/')
def login():
    return render_template("login.html")

@app.route('/logout/')
def logout():
    return redirect(url_for('root')) # Δίνω το όνομα της σελίδα όπως είναι το όνομα της μεθόδου, δηλαδή root και όχι index ή κάτι άλλο.

@app.route('/new_article/')
def new_article():
    return render_template("new_article.html")

if __name__ == "__main__":
    app.run(debug=True)