from flask import Flask, request, redirect, url_for, session, Response


app = Flask(__name__)
app.secret_key = "supersecret"


@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")


        if username == "admin" and password == "123":
            session["user"] = username # store in session
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid Credentials. Try again", mimetype="text/plan")

    return '''
        <h2>Login Page</h2>
        <form method="POST">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="text" name="password"><br><br>
        <input type="submit" value="Login">

        </form>
'''


# after login 
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome, {session["user"]}!</h2>
        <a href={url_for('logout')}>Logout</a>
'''
    return redirect(url_for('login'))



@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for('login'))
         








if __name__ == "__main__":
    app.run(debug=True)