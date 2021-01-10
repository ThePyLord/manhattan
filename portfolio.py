#TODO: Create a portfolio tracker that the bot can use
import json

""" try:
	with open("database.json", "r+") as f:
		user_data = json.load(f) #load the file into a Python object
except Exception as e:
	print(e)
finally:
	user_data.close() """


class Portfolio:
	"""
	Create a portfolio for a user 
	"""
	def __init__(self):
		self.portfolio = {}
		self.pft_data = json.loads(self.portfolio)

	#Set the percentage change which the user should be notified of
	def set_notif(self, notif):
		self.trgs = []
		self.trgs.append(notif)
		return self.trgs

	#Another way to implement an update is to use member variables
	def update_portfolio(self, tick_name, entry, **kwargs):
		# Use the official ticker symbol
		self.portfolio["tick_name"] = str(tick_name).upper()
		self.portfolio["entry"] = entry
		self.portfolio["target"] = kwargs["target"]


drews_pft = Portfolio()

