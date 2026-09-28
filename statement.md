# Project Statement

## Hostel Mess Management System

---

## 📌 Problem Statement

In most hostels, mess expenses are shared among all students, but individual food consumption varies — some students eat all three meals a day, while others skip meals due to outings, illness, or personal choice. When the total mess bill is split equally among everyone, students who eat less end up subsidising those who eat more, which is unfair and frequently leads to disputes.

Manually tracking attendance and expenses on paper or in spreadsheets is time-consuming, error-prone, and hard to maintain over an entire semester. There is a need for a simple, low-cost system that records daily meal attendance and expenses, and automatically calculates a fair, usage-based bill for each student.

---

## 🎯 Scope of the Project

This project is a **command-line application** built in Python that:

- Maintains a list of registered students.
- Records the number of meals (0–3) eaten by each student per day.
- Records daily mess expenses (item and amount).
- Calculates a per-meal rate by dividing total expenses by total meals consumed.
- Generates a bill for each student based on their individual meal count.
- Stores all data persistently in plain text files, requiring no external database.

**In scope:**
- Single mess / single hostel usage.
- Text-file based storage and a console-based interface.
- Basic input validation (duplicate students, invalid meal counts, invalid expense amounts).
- Automated testing of core logic.

**Out of scope:**
- Graphical or web-based user interface.
- Multi-mess or multi-hostel support.
- User authentication / login system.
- Online payments or integration with banking systems.
- Monthly/period-wise billing cycles (current version calculates lifetime totals).

---

## 👥 Target Users

- **Mess managers / mess secretaries** who are responsible for tracking student attendance, daily expenses, and generating bills.
- **Hostel wardens or administrators** who need a simple, transparent way to oversee mess accounts without manual calculation.
- **Small hostels or student groups** that want a low-cost, no-installation-hassle tool instead of paid software or complex spreadsheets.
- **Students** (indirectly) who benefit from fair, consumption-based billing instead of equal-split billing.

---

## 🧩 High-Level Features

1. **Student Registration**
   - Add new students with duplicate and empty-name checks.

2. **Attendance Tracking**
   - Record daily meals (0–3) for each registered student.
   - Reject attendance entries for unregistered students or invalid meal counts.

3. **Expense Logging**
   - Record daily mess expenses with item name and amount.
   - Validate that amounts are numeric and greater than zero.

4. **Automatic Bill Calculation**
   - Compute a per-meal rate from total expenses and total meals.
   - Generate each student's bill proportional to their meal count.

5. **Mess History Report**
   - Display total days recorded, total expense, and a sorted summary of each student's meals and bill.

6. **Persistent Storage**
   - Save all data to plain text files so it is retained between program runs.

7. **Automated Testing**
   - A dedicated test script validates core functionality (adding students, marking attendance, logging expenses, and bill calculation) using isolated test data.
