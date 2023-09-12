from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True)
