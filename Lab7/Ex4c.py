#On your own
#Create a function iterating through recent purchases and
#  write test cases for this and use them to test the function.

recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 50

def check_purchases(purchases, budget):
    total_spent = 0
    for purchase in purchases:
        total_spent += purchase
        if total_spent > budget:
            print(f"This purchase {purchase} is over budget")
        else:
            print(f"This purchase {purchase} is within budget")

purchase_list = [12.98, 34, 58.20, 22.91, 88.03, 19, 100, 28.63, 99.99, 0.78, 21.50, 12.00, 25.01]
budget_list = [12.98, 90, 10.99, 52.03, 30, 75.89, 100, 50, 60.56, 40.00, 20, 90, 25]

def test_check_purchases(purchases, budgets):
    for purchase, budget in zip(purchases, budgets):
        if purchase > budget:
            print(f"Purchase ${purchase:.2f} is over budget (${budget:.2f}).")
        else:
            print(f"Purchase ${purchase:.2f} is within budget (${budget:.2f}).")

test_check_purchases(purchase_list, budget_list)