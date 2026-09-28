from datetime import date
from DataStorage import readrow, addrow

EXPENSES = "expenses.txt"
Expenses = EXPENSES


def add(item, amount):
    try:
        amount = float(amount)
    except ValueError:
        return "Amount must be a number."
    if amount <= 0:
        return "Amount must be greater than 0."
    addrow(EXPENSES, [date.today(), item.strip().replace(",", " "), amount])
    return "saved"


def daily(item, amount):
    return add(item, amount)


def total():
    expense = 0.0
    for row in readrow(EXPENSES):
        expense = expense + float(row[2])
    return expense