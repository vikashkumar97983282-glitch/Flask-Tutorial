from flask import Flask, request, Response, url_for, redirect, render_template
from form import RegistrationForm



app = Flask(__name__)


@app.route("/")
def start():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":

        Name = request.form.get("name")
        Username = request.form.get("username")
        Password = request.form.get("password")

        if Username == 'admin' and Password == "1234":
            return render_template('home.html')


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/content")
def content():
    return render_template("content.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")










if __name__ == "__main__":
    app.run(debug=True)