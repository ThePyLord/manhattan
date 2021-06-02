from mongoengine import Document, DictField, ListField, IntField
from portfolio import Portfolio


#TODO: Set this Schema as a standard for the structure of the database
class PortfolioSchema(Document):
    portfolio = DictField(required=True)
    notifs = ListField(IntField())
    username = ListField(DictField(portfolio))

