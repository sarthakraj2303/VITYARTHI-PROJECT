from Students import add,mark
from Expenses import daily
from History import show

def main():
    print("Welcome to hsostel mess Choose one of option given below:")
    print("\n1.Add Student  2.Mark attendance  3.Add expense  4.Mess History  5.Exit")
    return input("Enter your choice:")

while True:
    choice = main()
    if choice == "1":
        print(add(input("Name: ")))
    elif choice == "2":
        print(mark(input("Name: "), input("Meals today (0-3): ")))
    elif choice == "3":
        print(daily(input("Item: "), input("Amount: ")))
    elif choice == "4":
        show()
    elif choice == "5":
        print("Bye! Have a nice day")
        break
    else:
        print("Invalid choice, try again.")