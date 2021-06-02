from flask import Flask, request, jsonify, make_response
from flask_restful import Api
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
try:
	client = MongoClient(
		host='localhost',
		port=27017,
		serverSelectionTimeoutMS=1000
	)
	# Trigger exception if connection fails
	client.server_info()
	manhattan_db = client.manhattan
	portfolio_col = manhattan_db['portfolios']
except:
	print('Failed to Connect to the database')



# class Portfolio(db.Model):
# 	pass


@app.route('/')
def index():
	return "Hello"


@app.route('/portfolios')
def portfolios():
	return jsonify({"message":  "You are at the /portfolios route"}), 200


@app.route('/portfolios/add', methods=['POST'])
def add():
	if request.method == 'POST':
		if request.is_json:
			req = request.get_json()
			portfolio_col.insert_one(req)
			res = {'message': 'message received'}
		return jsonify(res), 200
	else:
		return jsonify({"message": "you requested the root route"}), 200

@app.route('/portfolios/delete/<asset>', methods=['DELETE'])
def remove_asset(asset):
	return jsonify(message='Item deleted!👍')

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8000, debug=True)
