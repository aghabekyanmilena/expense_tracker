from tracker import Tracker

def main():
	tracker = Tracker()
	tracker.load_file()

	try:
		while True:
			print("\nWelcome to your Expense Tracker!")
			print("1. Add expense")
			print("2. View all expenses")
			print("3. View statistics")
			print("4. Save and exit")

			choice = input("> ")

			if choice == "1":
				while True:
					try:
						amount = float(input("Enter amount: "))
						break
					except ValueError:
						print("Invalid amount! Please enter a number.")
				category = input("Enter category: ")
				description = input("Enter description: ")
				tracker.add_expense(amount, category, description)
			elif choice == "2":
				tracker.view_expenses()
			elif choice == "3":
				total = sum(e.amount for e in tracker.expenses)
				print(f"Total spent: {total}")
			elif choice == "4":
				tracker.save_to_file()
				print("Expenses saved!")
				break
			else:
				print("Invalid choice, try again.")
	except KeyboardInterrupt or EOFError:
		print("\nExiting program.")

if __name__ == "__main__":
	main()
