from datetime import datetime

class Expense:

	def __init__(self, amount, category, description, date = None):
		self.amount = amount
		self.category = category
		self.description = description
		self.date = date if date else datetime.now().strftime("%Y-%m-%d")

	def __str__(self):
		return f"{self.date} | {self.category} | {self.amount} | {self.description}"