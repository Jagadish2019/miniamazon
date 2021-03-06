from pymongo import MongoClient
from bson.objectid import ObjectId

# mongodb written in javascript

client = MongoClient()
db = client['amazon']

def user_exists(username):
	query = {'username' : username}
	result = db['users'].find(query)

	if result.count() > 0:
		return True
	return False

def add_product(product):
	db['products'].insert_one(product)

def product_exists(product_name):
	query = {'name' : product_name}
	result = db['products'].find(query)

	if result.count() > 0:
		return True
	return False


def create_user(user_info):
	db['users'].insert_one(user_info)


def login_user(username):

	query = {'username':username}
	result = db['users'].find_one(query)

	return result

def buyer_products():
	result = db['products'].find({})
	return result

def seller_products(username):
	result = db['products'].find({'seller':username})
	return result

def add_to_cart(product_id, username):
	#db['users'].update({'username':username},{"$addToSet":{"cart":{"$each":[product_id]}}}) # Its a list
	query = {'username':username}
	result = db['users'].find_one(query)
	if result['cart'].get(product_id):
		db['users'].update({'username':username},{"$inc":{f"cart.{product_id}":1}})
		return True
	db['users'].update({'username':username},{"$set":{f"cart.{product_id}":1}})


def remove_from_cart(product_id, username):
	#db['users'].update({'username':username},{"$addToSet":{"cart":{"$each":[product_id]}}}) # Its a list
	query = {'username':username}
	result = db['users'].find_one(query)
	if result['cart'].get(product_id)<=1:
		db['users'].update({'username':username},{"$unset":{f"cart.{product_id}":1}})
		return True
	db['users'].update({'username':username},{"$inc":{f"cart.{product_id}":1}})

def cart_info(username):
	query = {'username':username}
	result = db['users'].find_one(query)['cart'].keys()

	products = []
	quantity = []
	for product_id in result:
		products.append( db['products'].find_one({'_id':ObjectId(product_id)}))
		quantity.append( db['users'].find_one({'username':username})['cart'][product_id])
	
	return (products,quantity)

	