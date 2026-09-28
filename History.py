from DataStorage import readrow
import Students
from Expenses import total


def Bills():
    count = Students.meals()
    total_meals = sum(count.values())
    if total_meals == 0:
        return {}
    rate = total() / total_meals
    bills = {}
    for name in count:
        bills[name] = round(count[name] * rate, 2)
    return bills


def show():
    days = set(row[0] for row in readrow(Students.ATTENDANCE))
    bills = Bills()
    count = Students.meals()
    print("\nDays recorded:", len(days))
    print("Total expense: Rs", total())
    rows = [(name, count[name], bills[name]) for name in bills]
    rows.sort(key=lambda r: r[2], reverse=True)
    for name, meal_count, bill in rows:
        print(name, " meals: ", meal_count, " bill: Rs ", bill)