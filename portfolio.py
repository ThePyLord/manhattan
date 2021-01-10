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
		self.notifs = [0.2]
		self.notifs.sort()
		

	#Set percentage changes where the user would be notified at
	def set_notif(self, *args):
		for arg in list(args):
			self.notifs.append(arg)


	#Another way to implement an update is to use member variables
	def update_portfolio(self, tick_name, entry, **kwargs):
		# Use the official ticker symbol
		self.portfolio["tick_name"] = 
		(tick_name).upper()
		self.portfolio["entry"] = float(entry)
		self.portfolio["target"] = round(kwargs["target"], 2)

	def export_data(self):
		pass

#test portfolio
drews_pft = Portfolio()