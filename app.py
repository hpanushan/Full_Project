from flask import Flask, send_file, render_template, request

app = Flask(__name__, )

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/static/twitter')
def twitter():
    return render_template('index.html')

@app.route('/static/facebook')
def facebook():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

