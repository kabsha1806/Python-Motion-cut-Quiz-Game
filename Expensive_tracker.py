import csv
from datetime import datetime

# Function to input expenses
def input_expense():
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category: ")
    date = datetime.now().strftime("%Y-%m-%d")
    return {'date': date, 'amount': amount, 'category': category}

# Function to save expenses to a CSV file
def save_expense(expense):
    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'amount', 'category'])
        writer.writerow(expense)

# Function to categorize expenses
def categorize_expenses(expenses):
    categories = {}
    for expense in expenses:
        category = expense['category']
        if category not in categories:
            categories[category] = []
        categories[category].append(expense['amount'])
    return categories

# Function to calculate monthly summary
def monthly_summary(expenses):
    monthly_totals = {}
    for expense in expenses:
        month = expense['date'][:7]
        amount = expense['amount']
        if month not in monthly_totals:
            monthly_totals[month] = 0
        monthly_totals[month] += amount
    return monthly_totals

# Main function
def main():
    expenses = []
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Input Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Expenditure")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            expense = input_expense()
            save_expense(expense)
            expenses.append(expense)
            print("Expense recorded successfully!")

        elif choice == '2':
            monthly_totals = monthly_summary(expenses)
            for month, total in monthly_totals.items():
                print(f"{month}: ${total}")

        elif choice == '3':
            categories = categorize_expenses(expenses)
            for category, amounts in categories.items():
                total = sum(amounts)
                print(f"{category}: ${total}")

        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
