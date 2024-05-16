from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_tesoriere')
def login_tesoriere():
    return render_template('login_tesoriere.html')

@app.route('/login_socio')
def login_socio():
    return render_template('login_socio.html')

if __name__ == '__main__':
    app.run(debug=True)
