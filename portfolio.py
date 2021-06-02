#TODO: Create a portfolio tracker that the bot can use
#TODO: Add a quantity of the asset purchased
import json

class Portfolio:
	"""
	Create a portfolio for a user

	Attributes:	
	-----------
	portfolio: 
	"""
	_instances = 0

	def __init__(self):	
		Portfolio._instances += 1
		self.portfolio = {}
		self.notifs = [0.2]

	def __str__(self):
		return """ The users's portfolio """

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
		self.portfolio["entry"] = float(entry)
		self.portfolio["target"] = float(kwargs.get("target"))
		# self.portfolio["quantity"] = float(kwargs.get("quantity"))

		return "Portfolio has been updated"


	def to_json(self):
		return json.dumps({
			"portfolio": self.portfolio,
			"notifs": self.notifs
		})
