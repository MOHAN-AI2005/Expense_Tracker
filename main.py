import csv
from datetime import datetime

filename = "expenses.csv"

def add_expense(amount, category):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), amount, category])

def view_expenses():
    try:
        with open(filename, mode='r') as file:
            for row in csv.reader(file):
                print(row)
    except FileNotFoundError:
        print("No expenses found.")

while True:
    action = input("Add or view expenses? (a/v/exit): ").strip().lower()
    if action == 'a':
        amt = float(input("Amount: "))
        cat = input("Category: ")
        add_expense(amt, cat)
    elif action == 'v':
        view_expenses()
    elif action == 'exit':
        break
