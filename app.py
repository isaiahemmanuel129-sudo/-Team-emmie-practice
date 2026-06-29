from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    print("Perfect!!!")
    return render_template('emmie.html')

if __name__ == '__main__':
    app.run(debug=True)