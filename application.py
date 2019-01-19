from flask import Flask
import os
app = Flask(__name__)


@app.route("/")
def main():
    return "Hello, world"
    return render_template(os.path.join('templates', 'main.html'))
