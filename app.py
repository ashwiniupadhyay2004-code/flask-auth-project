from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

# Home → go to signup
@app.route('/')
def home():
    return redirect('/signup')

# Signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
        c.execute("INSERT INTO users VALUES (?, ?)", (username, password))

        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('signup.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        user = c.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        ).fetchone()

        conn.close()

        if user:
            session['user'] = username
            return redirect('/dashboard')

    return render_template('login.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    return render_template('dashboard.html', user=session['user'])

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)
   
   
