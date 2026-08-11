from flask import Flask


app = Flask(__name__)

@app.route('/', methods=["GET"])
def welcome():
    return "<h1>Hii, welcome to our flask frameworks!</h1>"

@app.route('/index', methods=["GET"])
def index():
    return "<h1>This is our index pages!</h1>"



if __name__ =="__main__":
    app.run(debug=True)