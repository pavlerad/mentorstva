# from methods import load_file, save_file, delete_file




#products = load_file("data/products.json")
#users = load_file("data/user.json")
#print(products,"\n",users)

import json
import random
import calendar
from datetime import datetime
date = datetime.now()

user = None
import sys

expense = 0

with open ("user.json", "r") as file:
    user = json.load(file)
    print(f"Your budget is: {user["budget"]: .2f} EUR.")

def max_budget():
    return random.randint(0, 2000)
print(f"The maximum budget for {date} is: {max_budget():.2f} EUR")

user_budget = user["budget"] + user["credit"]
print(f"The summary of the credit and the budget is {user_budget:.2f} EUR")

if user_budget <= 0:
    print("Your budget cannot be equal or below 0.")
elif user["budget"] >= max_budget():
    print(f"Following our calculations, your budget cannot be accepted since it surpasses the budget maximum for {date}, which is {max_budget():.2f} EUR.")
else:
    print(f"Your budget is accepted, since it does not surpass our maximum budget for {date}, which is: {max_budget():.2f} EUR.\n")

input("\nPress the enter key to exit.")

expense = 0

while expense <= 0:
    expense = int(input("Please enter your budget: "))
print(f"Your expenses are equal to {expense:.2f} EUR.")

while expense <= 0 or expense > user_budget:
    int(input("Please enter your budget: "))



with open ("../../logs/expense_log.txt", "w") as file:
    remaining_budget = user_budget - expense
    message = (f"Amount: {expense}, "
               f"User_id: {user["id"]}, "
               f"user_budget: {user_budget}, "
               f"remaining_budget: {remaining_budget},"
               f"datetime: {datetime.now()}")
    file.write(message)