from flask import Flask, render_template, url_for, request, session, abort, flash, redirect
import mysql.connector

app = Flask(__name__)
SECRET_KEY = 'test'

app.config.from_object(__name__)

@app.route('/')
def show_entries():
    conn = mysql.connector.connect(
            host = 'localhost', 
            port = 3306,
            user = 'root',
            passwd = 'xiaomin',
            db = 'test'
            )
    cur = conn.cursor()
    cur.execute('select title, text from entrie order by id desc')
    entries = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    return render_template('test.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    conn = mysql.connector.connect(
            host = 'localhost', 
            port = 3306,
            user = 'root',
            passwd = 'xiaomin',
            db = 'test'
            )
    cur = conn.cursor()
    cur.execute('insert into entrie (title, text) values (%s, %s)',
               (request.form['title'], request.form['text']))
    cur.close()
    conn.commit()
    conn.close()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/test')
def t():
    return render_template('python.html')

if __name__ == '__main__':
    app.run(debug=True)
