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
<<<<<<< HEAD

	def __str__(self):
		return """ """
=======
		print("Portfolio has been registered")
		
>>>>>>> Il-grande-Finale

	#Set percentage changes where the user would be notified at
	def set_notif(self, *args):
		""" """
		for arg in list(args):
			self.notifs.append(arg)
		self.notifs.sort()


	#Another way to implement an update is to use member variables
	def update_portfolio(self, tick_name, entry, **kwargs):
		# Use the official ticker symbol
		self.portfolio["tick_name"] = str(tick_name).upper()
		self.portfolio["entry"] = float(entry)
		self.portfolio["target"] = kwargs.get("target")


	def export_data(self):
		self.profile = {
			"portfolio": self.portfolio,
			"notifs": self.notifs
		}
		return self.profile

	

#test portfolio
drews_pft = Portfolio()
<<<<<<< HEAD
<<<<<<< Updated upstream
# drews_pft.update_portfolio('btc', 1500, target=10000)
=======
>>>>>>> Stashed changes
=======
>>>>>>> Il-grande-Finale
