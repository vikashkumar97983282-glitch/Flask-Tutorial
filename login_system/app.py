from flask import Flask, request, redirect, Response, session, url_for, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("loginpage.html")

    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "1122":
        return render_template("welcome.html", name=username)
    else:
        return "Invalid username or password"









if __name__ == "__main__":
    app.run(debug=True)