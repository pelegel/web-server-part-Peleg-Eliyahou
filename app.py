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
    artists = {'maroon 5': 'Band', 'justin bieber': 'Male singer', 'taylor swift': 'female Singer',
               'lady gaga': 'Female Singer', 'noa kiler': 'Female Singer'}
    females = []
    males = []
    bands = []
    tools = ('html', 'css', 'JavaScript','flask')
    return render_template('assignment3_1.html', artists=artists, tools=tools, females=females, males=males, bands=bands)




if __name__ == '__main__':
    app.run(debug=True)