from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template

app = Flask(__name__)


# root of our website
@app.route('/')
@app.route('/home')
def index_func():
    return render_template('home.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')



@app.route('/assignment3_1')
def assignment3_1_page():
    artists = ('Maroon 5', 'Justin Bieber','Taylor Swift','Lady Gaga', 'Noa Kiler')
    return render_template('assignment3_1.html',
                           artists=artists)




if __name__ == '__main__':
    app.run(debug=True)