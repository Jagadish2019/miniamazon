from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/') # decorator
def home():
	# return "hello world"
	return render_template('home.html',title="a2z products",name="Developed by Jagan",home = 'home')

@app.route('/about') # decorator
def about():
	# return "Jagadish"
	return render_template('about.html')

@app.route('/contact')
def contact():
	# return "Python is a interpreter, My name is Jagadish and I am a Python geek"
	return render_template('contact.html', title='contact')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/login',methods = ['POST'])
def login():

	user = {'username':'jagan','password':'12345'}

	username = request.form['username']
	password = request.form['password']

	if user['username'] == username:
		if user['password'] == password:
			return redirect(url_for('welcome'))
		return "wrong password, go back and try again!"
	return "this user doesn't exist. Go back and enter a valid user"


if __name__ == '__main__':
	app.run(debug=True)


