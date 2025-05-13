import json
import os
from datetime import date



date = date.today()
from datetime import datetime
import sys

with open("podaci.json", "r") as file:
    data = json.load(file)
    print(f"Your bank amount for {date} is: {data['bank_amount']: .2f} EUR.")

withdrawal = 0
expenses = 0



while withdrawal <= 0 or withdrawal >= data['bank_amount']:
    withdrawal = int(input("Please enter your the amount you want to withdrawal (it cannot exceed your bank amount): "))
    print(f"Your current budget is{withdrawal: .2f} EUR")
    data['bank_amount'] -= withdrawal
    print(f"Your total bank amount now is {data['bank_amount']: .2f}EUR")

expenses = int(input("Please enter your expenses: "))

while expenses > withdrawal or expenses >= data['bank_amount']:
    print("Expenses cannot be greater than your withdrawal nor your bank total.")
    expenses = int(input(f"Please enter your expenses for {date}: "))
    sys.exit()

remaining_budget =  withdrawal - expenses
print(f"Your remaining budget is {remaining_budget: .2f} EUR.")
# data['bank_amount'] -= withdrawal + expenses + remaining_budget
data['bank_amount'] += remaining_budget
print(f"Your bank total now is {data['bank_amount']: .2f}EUR.")


with open("../bank_logs/logovi.txt", "a") as file:
    message =  f" bank amount: {data['bank_amount']}, remaining_budget: {remaining_budget}, withdrawal: {withdrawal}, bank_deposit: {data['bank_amount']}, time{datetime.now()}"
    file.write(message)

input("\nPress enter key to exit.")




  #  print(f"Your current budget is {withdrawal}.")



