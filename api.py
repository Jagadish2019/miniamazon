from flask import Flask, render_template, request, redirect, url_for, session # session is special dictionary
from models.model import user_exists, create_user, login_user, add_product, product_exists, seller_products, buyer_products, add_to_cart


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'


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

@app.route('/login',methods = ['POST','GET'])
def login():

	# user = {'username':'jagan','password':'12345'}
	if request.method == 'POST':

		username = request.form['username']
		password = request.form['password']

		user = login_user(username)

		if user is None:

			return "This user doesn't exist. Go back and enter a valid user"


		if user['username'] == username:
			if user['password'] == password:
				session['username'] = user['username']
				session['c_type'] = user['c_type']
				return redirect(url_for('home'))
				#return redirect(url_for('welcome'))
			return "wrong password, go back and try again!"
		return "this user doesn't exist. Go back and enter a valid user"
	else:
		return redirect(url_for('home'))



@app.route('/signup', methods = ['POST','GET'])

def signup():

	if request.method == 'POST':
	
		user_info = {}
		user_info['username'] = request.form['username']
		user_info['email'] = request.form['email']
		user_info['password'] = request.form['password']
		rpassword = request.form['rpassword']
		user_info['c_type'] = request.form['c_type']

		if user_exists(user_info['username']) is False:
			if user_info['password'] == rpassword:
				if user_info['c_type'] == 'buyer':
					user_info['cart'] = []
				create_user(user_info)
				session['username'] = user_info['username']
				session['c_type'] = user_info['c_type']
				return redirect(url_for('home'))
				#return render_template('welcome.html', user = user_info['username'])
			return "Passwords don't match. Re-enter the password accurately"
		return "user exists. Enter another username"
	else:
		return redirect(url_for('home'))


@app.route('/seller', methods=['GET','POST'])
def seller():

	if request.method == 'POST':
		product_info = {}

		product_info['name'] = request.form['name']
		product_info['price'] = int(request.form['price'])
		product_info['seller'] = session['username']
		product_info['description'] = request.form['description']

		if product_exists(product_info['name']) is False:
			add_product(product_info)
			return redirect(url_for('product'))
		return "product already exists. Go back and enter another product"


@app.route('/product')
def product():
	#import pdb; pdb.set_trace()

	if session['c_type'] == 'buyer':
		return render_template('products.html', products=buyer_products())
	return render_template('products.html', products=seller_products(session['username']))

	#return render_template('products.html')


@app.route('/addcart',methods=['POST'])
def add_cart():
	product_id = str(request.form['id'])
	add_to_cart(product_id,session['username'])
	return redirect(url_for('home'))

@app.route('/logout')
def logout():

	session.clear()
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True)

