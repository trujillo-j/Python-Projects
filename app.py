from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy 
import shortuuid 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

shortuuid.set_alphabet("abcfghjkmnprtubxyz1347095")

db = SQLAlchemy(app)

class urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key = True)
    longURL = db.Column("longURL", db.String())
    shortURL = db.Column("shortURL", db.String(3))

    def __init__(self, long, short = None):
        self.longURL = long
        if short is None:
            self.shortURL = shortuuid.uuid()[:4]
        else:
            self.shortURL = short 


with app.app_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        url_recieved = request.form["subURL"]
        submitted_urls = urls.query.filter_by(longURL = url_recieved).first() 
        if submitted_urls:
            foundEnd = urls.query.filter_by(longURL = url_recieved).first().shortURL
            return render_template("short.html", shortEnd = foundEnd)
        new_url = url_recieved
        db.session.add(urls(long = new_url))
        db.session.commit()
        urlEnd = urls.query.filter_by(longURL = new_url).first().shortURL

        return render_template("short.html", shortEnd = urlEnd)

    else:
        return render_template("home.html")

@app.route('/trujilloj') #unused directory, will remove later
def trujilloj():
    return redirect("https://github.com/trujillo-j/URL-Shortner")

@app.route('/display/<url>') #incomplete directory, need to complete html page and short_url_display function 
def display_shortURL(url):
    return render_template('short.html', short_url_display = url)

@app.route('/<short_URL>')
def redirection(short_URL):
    longURL = urls.query.filter_by(shortURL = short_URL).first().longURL
    if longURL:
            return redirect(longURL)
    else:
        return f'<h1>URL does not exist.</h1>'

if __name__ =='__main__':
    app.run(port=5000, debug=True) 