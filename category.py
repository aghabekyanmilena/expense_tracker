class Category:

	def __init__(self):
		self.categories = ["Food", "Transport", "Utilities",
					"Entertainment", "Other"]

	def add_category(self, newCategory):
		if newCategory not in self.categories:
			self.categories.append(newCategory)

	def view_category(self):
		return self.categories