from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Web app for saving receipt info to Monzo app!"
