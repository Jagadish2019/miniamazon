from pymongo import MongoClient

# mongodb written in javascript

client = MongoClient()
db = client['amazon']

def user_exists(username):
	query = {'username' : username}
	result = db['users'].find(query)

	if result.count() > 0:
		return True
	return False

def create_user(user_info):
	db['users'].insert_one(user_info)


def login_user(username):

	query = {'username':username}
	result = db['users'].find_one(query)

	return result




