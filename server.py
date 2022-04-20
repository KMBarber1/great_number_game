from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "keep it secret and safe"


@app.route('/')
def index():
    if 'num' not in session:
        session['num']=random.randint(1,101)
    if 'message' not in session:
        session["message"]=""
    print(session["num"])

    return render_template('index.html')



@app.route('/guess', methods=['POST'])
def guess():

    session['guess'] = int(request.form['guess'])

    # if 'guess' in session:
    if session['guess'] < session['num']:
        session['message'] = 'Too low guess higher!!!'
    elif session['guess'] > session['num']:
        session['message'] = 'Too high guess lower!!!'
    else:
        session['message'] = "You guessed the number!!!"

    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug = True, port = 5000)