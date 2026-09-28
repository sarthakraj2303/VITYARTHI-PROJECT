from datetime import date
from DataStorage import readrow, addrow

MEMBERS = "students.txt"
ATTENDANCE = "attendance.txt"
Students = MEMBERS
Attendance = ATTENDANCE


def get():
    return [row[0] for row in readrow(MEMBERS)]


def add_member(name):
    name = (name or "").strip().lower()
    if name == "":
        return "Name can't be empty"
    if name in get():
        return "Member already exists."
    addrow(MEMBERS, [name])
    return "Member added."


def add(name):
    return add_member(name)


def mark(name, meals):
    name = (name or "").strip().lower()
    if name not in get():
        return "Member not found."
    if not str(meals).isdigit() or int(meals) > 3:
        return "Must be a number from 0 to 3."
    addrow(ATTENDANCE, [date.today(), name, meals])
    return "Attendance saved."


def meals():
    count = {}
    for day, name, meal_count in readrow(ATTENDANCE):
        count[name] = count.get(name, 0) + int(meal_count)
    return count
