# 🍽️ Hostel Mess Management System 🍽️

A simple, menu-driven command-line application written in Python to manage a hostel mess: register students, record daily meal attendance, log mess expenses, and automatically calculate each student's bill based on the meals they have eaten.

---

## 📖 Overview


Running a hostel mess involves tracking who ate how many meals and splitting the total food expense fairly. This project automates that process.

- Students are registered once.
- Each day, the number of meals (0–3) eaten by a student is recorded.
- Daily expenses (rice, vegetables, gas, etc.) are recorded with an amount.
- The system divides the **total expense by the total meals eaten** to get a per-meal rate, then multiplies it by each student's meals to produce a fair bill.

All data is stored in plain text (CSV-style) files, so no database or external library is required.

---

## ✨ Featuresc

- **Add students** – names are normalised (trimmed, lowercase) and duplicates are rejected.
- **Mark attendance** – record 0–3 meals per student per day, with validation for unknown students and invalid numbers.
- **Add expenses** – record an item and amount; invalid, non-numeric, zero or negative amounts are rejected.
- **Mess history / billing** – shows number of days recorded, total expense, and each student's meal count and bill (sorted from highest to lowest bill).
- **Fair bill calculation** – `bill = student's meals × (total expense ÷ total meals)`.
- **Persistent storage** – data is saved in text files and reloaded on every run.
- **Automated tests** – a test script verifies the core logic using isolated temporary files (your real data is not touched).

---

## 🛠️ Technologies / Tools Used

| Tool | Purpose |
|------|---------|
| **Python 3.6+** | Core programming language |
| `datetime` (standard library) | Stamping attendance and expenses with today's date |
| `os` (standard library) | File cleanup in the test script |
| Plain text files (`.txt`) | Lightweight data storage (comma-separated rows) |

No third-party packages are needed.

---

## 📁 Project Structure

The files are listed in the order in which they build on each other:

```
.
├── DataStorage.py   # Low-level helpers to read/append rows in text files
├── Students.py      # Add students, mark attendance, count meals per student
├── Expenses.py      # Add expenses and calculate the total expense
├── History.py       # Calculates bills and prints the mess summary
├── menu.py          # Main entry point – interactive console menu
└── TestData.py      # Automated tests for the core logic
```

| File | Description |
|------|-------------|
| `DataStorage.py` | Provides `readrow(filename)` (returns all non-empty rows as lists, or `[]` if the file doesn't exist) and `addrow(filename, row)` (appends a comma-separated row). |
| `Students.py` | Manages `students.txt` and `attendance.txt`. Functions: `add_member` / `add`, `mark`, `get`, `meals`. |
| `Expenses.py` | Manages `expenses.txt`. Functions: `add` / `daily`, `total`. |
| `History.py` | `Bills()` computes each student's bill; `show()` prints the summary report. |
| `menu.py` | The interactive menu the user runs. |
| `TestData.py` | Asserts the expected behaviour of adding, marking, expenses, and bill calculation. |

**Data files (created automatically at runtime):**

- `students.txt` – one student name per line
- `attendance.txt` – `date,name,meals`
- `expenses.txt` – `date,item,amount`

---

## ⚙️ Steps to Install & Run

### 1. Prerequisites

Make sure Python 3.6 or newer is installed:

```bash
python -- 3.14.7
```

### 2. Clone the repository

```bash
git clone https://github.com/<sarthakraj2303>/<VITYARTHI-PROJECT>.git
cd <VITYARTHI-PROJECT>
```

### 3. Install dependencies

None required – the project uses only the Python standard library.

### 4. Run the application

```bash
python menu.py
```

### 5. Using the menu

```
Welcome to hostel mess. Choose one of the options given below:

1.Add Student  2.Mark attendance  3.Add expense  4.Mess History  5.Exit
Enter your choice:
```

| Option | Action | Prompts |
|--------|--------|---------|
| `1` | Add a student | Name |
| `2` | Mark attendance for today | Name, meals today (0–3) |
| `3` | Add an expense | Item, amount |
| `4` | View mess history and bills | – |
| `5` | Exit | – |

### Example session

```
Enter your choice:1
Name: Sarthak
Member added.

Enter your choice:1
Name: Utpal
Member added.

Enter your choice:2
Name: Sarthak
Meals today (0-3): 3
Attendance saved.

Enter your choice:2
Name: Utpal
Meals today (0-3): 1
Attendance saved.

Enter your choice:3
Item: Paneer
Amount: 400
saved

Enter your choice:4

Days recorded: 1
Total expense: Rs 400.0
Sarthak  meals:  3  bill: Rs  300.0
Utpal  meals:  1  bill: Rs  100.0
```

---

## 🧪 Instructions for Testing

The project includes `TestData.py`, which tests the main features:

- adding students (including duplicate detection, case-insensitive)
- marking attendance (valid student, unknown student, invalid meal count)
- adding expenses (valid and non-numeric amounts)
- bill calculation (`ravi` → Rs 300, `amit` → Rs 100 for 4 meals and Rs 400 total)

### Run the tests

```bash
python TestData.py
```

### Expected output

```
All tests passed!
```

### Notes

- The tests redirect the program to **separate test files** (`StudentName.txt`, `StudentAttendance.txt`, `StudentExpenses.txt`), and these are deleted after the run.
- ⚠️ At the **start** of the test run, the script also deletes `students.txt`, `attendance.txt`, and `expenses.txt` if they exist in the folder. **Back up your real data before running the tests**, or run the tests in a separate copy of the project.
- If an assertion fails, Python raises an `AssertionError` pointing to the failing line.

---

## 📸 Screenshots

<img width="1901" height="1117" alt="main menu" src="https://github.com/user-attachments/assets/3e2e261f-9ed5-483c-a6fb-6d69c91a0590" />






