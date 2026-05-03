@app.route('/signup', methods=['GET', 'POST'])
def signup():

   from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/signup')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
        c.execute("INSERT INTO users VALUES (?, ?)", (username, password))

        conn.commit()
        conn.close()

        return redirect('/signup')

    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)
    