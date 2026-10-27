
## Features

* **Budget Validation:** Ensures initial budget input is valid (non-negative and non-zero numbers only).
* **Interactive Expense Logging:** Continuously prompts for expense descriptions, categories, and amounts until you type `done`.
* **Input Error Handling:** Validates expense amounts to reject negative numbers and handle invalid inputs gracefully.
* **Comprehensive Reporting:** Generates a detailed breakdown including:
  * Total amount spent
  * Remaining budget
  * Highest single expense recorded
  * Spending breakdown by category
* **Financial Health Status:** Evaluates your spending status against your budget (Healthy, Warning, Budget Fully Used, or Over Budget).

## File Structure

* `main.py` - The core Python script containing the logic for budget entry, expense tracking, and report generation.
* `test_cases.txt` - Contains predefined test scenarios and expected outputs for validating the program.
* `README.md` - Documentation for the project.
## Example Usage/Workflow
=== Personal Expense Auditor ===
Enter Budget: 5000
Add your expenses. Type 'done' when finished.
Description or 'done': Grocery
Category: Food
Amount: 1200
Description or 'done': Bus pass
Category: Transport
Amount: 600
Description or 'done': Movie tickets
Category: Entertainment
Amount: 400
Description or 'done': done

----- REPORT -----
Expenses:
- Grocery | Food | 1200.0
- Bus pass | Transport | 600.0
- Movie tickets | Entertainment | 400.0
Total Spent: 2200.0 | Remaining Budget: 2800.0
Highest Single Expense: Grocery, Food, 1200.0
Category Totals:
- Food: 1200.0
- Transport: 600.0
- Entertainment: 400.0
Budget Status: Healthy (44% used, within budget)

