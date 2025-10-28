from expense import Expense
import json

def log_action(func):
	def wrapper(*args, **kwargs):
		return func(*args, **kwargs)
	return wrapper

class Tracker:

	def __init__(self):
		self.expenses = []

	@log_action
	def add_expense(self, amount, category, description):
		expense = Expense(amount, category, description)
		self.expenses.append(expense)

	def view_expenses(self):
		for exp in self.expenses:
			print(exp)

	def save_to_file(self, filename="expenses.json"):
		with open(filename, "w") as json_file:
			json.dump([exp.__dict__ for exp in self.expenses], json_file, indent=4)

	def load_file(self, filename="expenses.json"):
		try:
			with open(filename, "r") as file:
				data = json.load(file)
				self.expenses = [
					Expense(
						item.get("_amount") or item.get("amount"),
						item.get("_category") or item.get("category"),
						item.get("_description") or item.get("description"),
						item.get("_date") or item.get("date")
					)
					for item in data
				]
		except FileNotFoundError:
			print("No saved file found")
