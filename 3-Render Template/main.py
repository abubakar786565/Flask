from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')



@app.route('/about')
def about():
    return render_template('Aboutus.html')



if __name__ == '__main__':
    app.run(debug=True)