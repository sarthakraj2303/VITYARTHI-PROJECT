import os
import Students
import Expenses
from History import Bills

for f in ("StudentName.txt", "StudentDate.txt", "StudentExpenses.txt", "StudentAttendance.txt", "students.txt", "attendance.txt", "expenses.txt"):
    if os.path.exists(f):
        os.remove(f)

Students.MEMBERS = "StudentName.txt"
Students.ATTENDANCE = "StudentAttendance.txt"
Expenses.EXPENSES = "StudentExpenses.txt"

assert Students.add_member("Sarthak") == "Member added."
assert Students.add_member("sarthak") == "Member already exists."
Students.add_member("Aditya")
assert Students.mark("Sarthak", "3") == "Attendance saved."
assert Students.mark("Aditya", "1") == "Attendance saved."
assert Students.mark("Drishya", "1") == "Member not found."
assert Students.mark("Swaraj", "9") != "Attendance saved."
assert Expenses.add("Chicken", "fifty") == "Amount must be a number."
assert Expenses.add("paneer", "200") == "saved"
assert Bills() == {"Sarthak": 200.0, "Aditya": 50.0}
print("All tests passed!")

for f in ("StudentName.txt", "StudentDate.txt", "StudentExpenses.txt", "StudentAttendance.txt"):
    if os.path.exists(f):
        os.remove(f)
