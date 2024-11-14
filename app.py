from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

with open('output.json') as file:
    matches = json.load(file)

@app.route('/')
def index():
    return render_template('index.html', matches=matches)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)