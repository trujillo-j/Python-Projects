from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        url_recieved = request.form["subURL"]
        return url_recieved
    else:
        return render_template("home.html")

@app.route('/trujilloj')
def trujillo():
    return "Mr. Trujillo, hi!"

if __name__ =='__main__':
    app.run(port=5000, debug=True)