from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Home working"

@app.route('/login')
def login():
    return "Login working"

if __name__ == "__main__":
    app.run(debug=True)