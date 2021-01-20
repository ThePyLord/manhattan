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

	Attributes:
	-----------
	portfolio: 
	"""

	def __init__(self):	
		self.portfolio = {}
		self.notifs = [0.2]

	def __str__(self):
		return """ """

		# print("Portfolio has been registered")
		

	#Set percentage changes where the user would be notified at
	def set_notif(self, *args):
		""" """
		for arg in list(args):
			self.notifs.append(arg)
		self.notifs.sort()


	#Another way to implement an update is to use member variables
	def update_portfolio(self, tick_name: str, entry: float, **kwargs):
		# Use the official ticker symbol
		self.portfolio["tick_name"] = tick_name.upper()
		self.portfolio["entry"] = entry
		self.portfolio["target"] = float(kwargs.get("target"))


	def export_data(self):
		self.profile = {
			"portfolio": self.portfolio,
			"notifs": self.notifs
		}
		return self.profile


