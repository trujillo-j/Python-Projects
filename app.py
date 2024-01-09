from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key = True)
    longURL = db.Column("longURL", db.String())
    shortURL = db.Column("shortURL", db.String(3))

    def __init__(self, long, short):
        self.longURL = long
        self.shortURL = short 


with app.app_context():
    db.create_all()

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