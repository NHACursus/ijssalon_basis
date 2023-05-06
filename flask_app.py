from flask import Flask
from flask import Flask, render_template

app=Flask(__name__)

if __name__ == '__main__':   
    app.run(port=5000,debug=True)


@app.route('/')
def home():    
    return  render_template("home.html")     # "Welkom op mijn eerste Flask-website"


'''
instead of using set FLASK_APP = flask_app.py, try $env:FLASK_APP = "flask_app.py"
'''


@app.route('/prijzen')
def prijzen():    
    items =[ { "product": "vanille-ijs 1 liter",   "prijs": "2 euro" },         
             { "product": "chocolade-ijs 1 liter", "prijs": "2 euro" } ]
    return render_template("prijzen.html", items=items)   # "Binnenkort verschijnen hier onze actuele prijzen"


@app.route('/recepten')
def recepten():
    items = [ { "recept": "Tiramisu di nona",       "img": "tiramisu.png" },         
              { "recept": "IJstaart met chocolade", "img": "ijstaart.png" } ]    
    return render_template("recepten.html", items=items)  # "Binnenkort verschijnen hier enkele recepten"



