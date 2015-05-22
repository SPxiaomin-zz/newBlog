from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    css = url_for('static', filename='bg.css')
    return render_template('index.html', css=css)

if __name__ == '__main__':
    app.run()
