from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # decorator
def home():
	# return "hello world"
	return render_template('home.html',title="a2z products",name="Developed by Jagan")

@app.route('/about') # decorator
def about():
	# return "Jagadish"
	return render_template('about.html')

@app.route('/contact')
def contact():
	# return "Python is a interpreter, My name is Jagadish and I am a Python geek"
	return render_template('contact.html')

if __name__ == '__main__':
	app.run(debug=True)


