from flask import render_template
from flask import request
from app import app
from app import process_data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['cointype']:
            enteredCoin = request.form['cointype']
        else:
            # if no value from form, default to 'bitcoin'.
            enteredCoin = "bitcoin"
        return render_template("index.html", data=process_data.process(enteredCoin),
            process_coins=process_data.process_coins(),
            enteredCoin=enteredCoin)
    elif request.method == 'GET':
        # set to 'bitcoin' when GET request.
        enteredCoin = "bitcoin"
        return render_template("index.html", data=process_data.process(enteredCoin),
            process_coins=process_data.process_coins())
