# Personal Expense Auditor

print("=== Personal Expense Auditor ===")

# ----- Step 1: get the budget -----
while True:
    text = input("Enter Budget: ")
    if text.startswith("-"): #Checking negative
        print("Budget cannot be negative.",text)
    elif text.isdigit():#confirming is digit or not
        budget = float(text) #Casting
        if budget == 0:
            print("Budget cannot be zero. Try again.")
        else:
            break
    else:
        print("Please enter a number, like 5000.")

# ----- Step 2: get the expenses -----
expenses = []
print("Add your expenses. Type 'done' when finished.")

while True:
    description = input("Description or 'done'): ")
    if description.lower() == "done":
        break

    category = input("Category: ")

    while True:
        text = input("Amount: ")
        if text.startswith("-"):
            print("Amount cannot be negative. Try again.")
        elif text.replace(".", "", 1).isdigit():
            amount = float(text)
            break
        else:
            print("Please enter a number, like 1200.")

    expense = {"description": description, "category": category, "amount": amount}
    expenses.append(expense)

# ----- Step 3: show the report -----
print("\n----- REPORT -----")

if len(expenses) == 0:
    print("No expenses entered.")
    print("Total Spent: 0 | Remaining Budget:", budget)
else:
    total = 0
    highest = expenses[0]
    category_totals = {}

    print("Expenses:")
    for item in expenses:
        print(" -", item["description"], "|", item["category"], "|", item["amount"])
        total = total + item["amount"]

        if item["amount"] > highest["amount"]:
            highest = item

        cat = item["category"]
        if cat in category_totals:
            category_totals[cat] = category_totals[cat] + item["amount"]
        else:
            category_totals[cat] = item["amount"]

    remaining = budget - total
    percent = total / budget * 100

    print("Total Spent:", total, "| Remaining Budget:", remaining)
    print("Highest Single Expense:", highest["description"], "(", highest["amount"], ")")

    print("Category Totals:")
    for cat in category_totals:
        print(" ", cat + ":", category_totals[cat])

    if total > budget:                                   #Total Spent greater than budget, get Negative you may take Barrow
        print("Budget Status: OVER BUDGET by", -remaining)
    elif total == budget:                                                #control your expenses
        print("Budget Status: Budget fully used. $0 remaining.")
    elif percent >= 80:                                                 #Yoyr in control
        print("Budget Status: Warning (", round(percent), "% used )")
    else:                                                               #Great Go like this
        print("Budget Status: Healthy (", round(percent), "% used, within budget )")