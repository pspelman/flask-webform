from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

user_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got post info...making new user"
    name = request.form['name']
    email = request.form['email']
    print "Name: {} || Email: {}".format(name, email)
    user_data[email]=name
    print user_data
    return success_page(name)

@app.route('/show')
def show_user():
    return render_template('user.html', name='Jay', email='jay@jay.com')



# @app.route('/success')
def success_page(user_name):
    message = "Congrats, {}, you submitted your email".format(user_name)
    print "Success page recieved {}".format(user_name)
    return render_template('success.html', message=message)

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print username
    print id
    return render_template("user.html")


# if __name__ == '__main__':
app.run(debug=True)

