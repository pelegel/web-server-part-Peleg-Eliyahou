from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template
from flask import request, session, jsonify

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
               'Lady gaga': 'Female Singer', 'noa kiler': 'Female Singer'}
    females = []
    males = []
    bands = []
    return render_template('assignment3_1.html', artists=artists, females=females, males=males, bands=bands)



@app.route('/assignment3_2')
def assignment3_2_page():
    if 'email' in request.args:
        email = request.args['email']

        if email == '':
            return render_template('assignment3_2.html',
                                   users_details=users_details)

        if email in emails:
            user_index = get_user_index(email)
            username = users_details[user_index]['name']
            user_password = users_details[user_index]['password']
            return render_template('assignment3_2.html',
                                   username=username,
                                   email=email,
                                   user_password=user_password)
        else:
            return render_template('assignment3_2.html',
                                   message='not found')
    else:
        return render_template('assignment3_2.html')









users = {'user1': {'name': 'Yossi', 'email': 'Yossi@gmail.com', 'password': 'Yossi12345'},
         'user2':  {'name': 'Dana', 'email': 'Dana@gmail.com', 'password': 'Dana12345'},
         'user3': {'name': 'Ron', 'email': 'Ron@gmail.com', 'password': 'Ron12345'},
         'user4': {'name': 'Noa', 'email': 'Noa@gmail.com', 'password': 'Noa12345'},
         'user5': {'name': 'Shir', 'email': 'Shir@gmail.com', 'password': 'Shir12345'}}

#list of user's details dictionaries
users_details = list(users.values())

# get all the user's emails list
emails =[]
for i in range(len(users_details)):
    emails.append(users_details[i]['email'])


# function to get the user's index in the users' dict
def get_user_index(email):
    for i in range(len(users_details)):
        if users_details[i]['email'] == email:
            return i

def printX():
    print('x')





if __name__ == '__main__':
    app.run(debug=True)


