from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to the Home Page!</h1>"


@app.route('/about')
def about():
    return "<h1>About Us</h1><p>This is the about page.</p>"

@app.route('/contact')
def contact():
    return "<h1>Contact Us</h1><p>This is the contact page.</p>"

if __name__ == '__main__':
    app.run(debug=True)