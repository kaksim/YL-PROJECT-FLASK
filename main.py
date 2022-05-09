from flask import Flask, render_template, url_for
from pprint import pprint
import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
pprint(data['Valute']['USD']['Value'])
usa = data['Valute']['USD']['Value']
pprint(data['Valute']['AUD']['Name'])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/79160/PycharmProjects/pythonProject/venv\Scripts/for_html/ex3/database.db'
db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))


@app.route('/')
@app.route('/index')
def index():
    return render_template('main_page.html')

@app.route('/home')
def home():
    return '<h1> О сайте инфа тут</h1>'

@app.route('/chats')
def chats():
    return 'Это для разработки чатов'

@app.route('/profile')
def profile():
    return 'профиль usera'

@app.route('/reg')
def reg():
    return render_template('registr.html')

@app.route("/log_reg")
def log_reg():
    return render_template("log_reg.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]

        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return redirect(url_for("work"))
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']

        register = user(username=uname, email=mail, password=passw)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")

@app.route('/tests')
def tests():
    return render_template('tests.html', title_tests='ВАЛЮТА', h1_tests='PAGE FOR TESTS', menu=menu, USA=usa)





@app.route('/work')
def work():
    return render_template('work.html', AUD_N=data['Valute']['AUD']['Value'], AUD_W=data['Valute']['AUD']['Previous'],
                           AZN_N=data['Valute']['AZN']['Value'], AZN_W=data['Valute']['AZN']['Previous'],
                           GBP_N=data['Valute']['GBP']['Value'], GBP_W=data['Valute']['GBP']['Previous'],
                           AMD_N=data['Valute']['AMD']['Value'], AMD_W=data['Valute']['AMD']['Previous'],
                           BYN_N=data['Valute']['BYN']['Value'], BYN_W=data['Valute']['BYN']['Previous'],
                           BGN_N=data['Valute']['BGN']['Value'], BGN_W=data['Valute']['BGN']['Previous'],
                           BRL_N=data['Valute']['BRL']['Value'], BRL_W=data['Valute']['BRL']['Previous'],
                           HUF_N=data['Valute']['HUF']['Value'], HUF_W=data['Valute']['HUF']['Previous'],
                           HKD_N=data['Valute']['HKD']['Value'], HKD_W=data['Valute']['HKD']['Previous'],
                           DKK_N=data['Valute']['DKK']['Value'], DKK_W=data['Valute']['DKK']['Previous'],
                           USD_N=data['Valute']['USD']['Value'], USD_W=data['Valute']['USD']['Previous'],
                           EUR_N=data['Valute']['EUR']['Value'], EUR_W=data['Valute']['EUR']['Previous'],
                           INR_N=data['Valute']['INR']['Value'], INR_W=data['Valute']['INR']['Previous'],
                           KZT_N=data['Valute']['KZT']['Value'], KZT_W=data['Valute']['KZT']['Previous'],
                           CAD_N=data['Valute']['CAD']['Value'], CAD_W=data['Valute']['CAD']['Previous'],
                           KGS_N=data['Valute']['KGS']['Value'], KGS_W=data['Valute']['KGS']['Previous'],
                           CNY_N=data['Valute']['CNY']['Value'], CNY_W= int(data['Valute']['CNY']['Previous']) / 10,
                           MDL_N=data['Valute']['MDL']['Value'], MDL_W=data['Valute']['MDL']['Previous'],
                           NOK_N=data['Valute']['NOK']['Value'], NOK_W=data['Valute']['NOK']['Previous'],
                           PLN_N=data['Valute']['PLN']['Value'], PLN_W=data['Valute']['PLN']['Previous'],
                           RON_N=data['Valute']['RON']['Value'], RON_W=data['Valute']['RON']['Previous'],
                           XDR_N=data['Valute']['XDR']['Value'], XDR_W=data['Valute']['XDR']['Previous'],
                           SGD_N=data['Valute']['SGD']['Value'], SGD_W=data['Valute']['SGD']['Previous'],
                           TJS_N=data['Valute']['TJS']['Value'], TJS_W=data['Valute']['TJS']['Previous'],
                           TRY_N=data['Valute']['TRY']['Value'], TRY_W=data['Valute']['TRY']['Previous'],
                           TMT_N=data['Valute']['TMT']['Value'], TMT_W=data['Valute']['TMT']['Previous'],
                           UZS_N=data['Valute']['UZS']['Value'], UZS_W=data['Valute']['UZS']['Previous'],
                           UAH_N=data['Valute']['UAH']['Value'], UAH_W=data['Valute']['UAH']['Previous'],
                           CZK_N=data['Valute']['CZK']['Value'], CZK_W=data['Valute']['CZK']['Previous'],
                           SEK_N=data['Valute']['SEK']['Value'], SEK_W=data['Valute']['SEK']['Previous'],
                           CHF_N=data['Valute']['CHF']['Value'], CHF_W=data['Valute']['CHF']['Previous'],
                           ZAR_N=data['Valute']['ZAR']['Value'], ZAR_W=data['Valute']['ZAR']['Previous'],
                           KRW_N=data['Valute']['KRW']['Value'], KRW_W=data['Valute']['KRW']['Previous'],
                           JPY_N=data['Valute']['JPY']['Value'], JPY_W=data['Valute']['JPY']['Previous']
                           )

@app.route('/ad')
def ad():
    return 'AD'



def info(code):
    name = data['Valute'][f'{code}']['Name']
    value = data['Valute'][f'{code}']['Value']
    previous = data['Valute'][f'{code}']['Previous']
    print(f'name - {name}, value - {value}, previous - {previous}')

info('AUD')





if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
