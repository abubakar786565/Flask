from flask import Flask

app = Flask(__name__)  # Initialize the Flask application

@app.route('/')  # Home route
def home():
    return "My Name is Abubakar Ikram"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)  # Run the Flask app on all interfaces