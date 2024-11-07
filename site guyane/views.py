from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

    

@app.route('/resultat',methods = ['POST'])
def resultat():
    result = request.form
    login  = result['login']
    password = result['password']
    if login =="1234" and password=="1234":
        return render_template("login_ok.html")
    else: 
        return render_template("erreur_login.html")

@app.route('/quizz.html',methods = ['GET'])
def quizz():
    return render_template("quizz.html")
    

app.run(debug=True)


