import json
import os
from calendar import monthcalendar
from datetime import date
date = date.today()
from datetime import datetime
import sys
import time
import calendar

msg = "\n----------------------------WELCOME TO DJILKOSH ATM------------------------------\n"

for x in msg:
    time.sleep(0.1)
    print(x, end = "")


with open("podaci.json", "r") as file:
    data = json.load(file)
    print(f"\nYour bank amount for {date} is: {data['bank_amount']: .2f} EUR.\n")

withdrawal = 0
expenses = 0
total_budget = 0
withdrawal_hist = []
expenses_hist = []

while withdrawal <= 0 or withdrawal >= data['bank_amount']:
    withdrawal = int(input(f"Please enter the amount you want to withdrawal - it cannot exceed your total bank amount: {data['bank_amount']: .2f}EUR): "))
    if withdrawal > data['bank_amount']:
        print("Error. The requested value is higher than your bank total.")
    else:
        print(f"You have made a withdrawal of funds: {withdrawal: .2f}EUR")
        withdrawal_hist.append(withdrawal)
        remaining_budget = data['bank_amount'] - withdrawal
        print(f"Your funds now are: {remaining_budget: .2f}EUR")

expenses = int(input("Please enter your expenses: "))
expenses_hist.append(expenses)


while expenses > withdrawal or expenses >= data['bank_amount']:
    print("Expenses cannot be greater than your withdrawal nor your bank total.")
    expenses = int(input(f"Please enter your expenses for {date}: "))


withdrawal -= expenses
print(f"Your remaining budget is: {withdrawal: .2f} EUR.")
total_budget = remaining_budget + withdrawal

print(f"Your total funds now are: {total_budget: .2f}EUR.")


#with open("../bank_logs/logovi.txt", "a") as file:
  #  message =  f" bank amount: {data['bank_amount']}, remaining_budget: {remaining_budget}, withdrawal: {withdrawal}, bank_deposit: {data['bank_amount']}, time{datetime.now()}"
  #  file.write(message)




options = ["ADD", "CURRENT", "WITHDRAWAL", "HISTORY_WITH", "HISTORY_EXP", "EXIT"]
choice = None
add = 0


while choice not in options:
    choice = input(f"Please choose how do you want to proceed ({", ".join(options)} ): ").upper()

    if choice == "ADD":
        add = int(input("Please choose the amount you want to add: "))
        while add > remaining_budget:
            add = int(input("Error. Please choose the amount you want to add: "))
        print(f"You have added {add: .2f} EUR to your bank account.")
        total_budget += add
        print(f"Your total budget now is: {total_budget: .2f}EUR")
        choice = None

    elif choice == "WITHDRAWAL":

        withdrawal = int(input("Please enter your the amount you want to withdrawal (it cannot exceed your bank amount): "))
        while withdrawal < 0 or withdrawal > total_budget:
            withdrawal = int(input("Please enter your the amount you want to withdrawal (it cannot exceed your bank amount): "))
        total_budget -= withdrawal
        print(f"Your total budget now is {total_budget: .2f} EUR.")
        # data['bank_amount'] -= withdrawal + expenses + remaining_budget
        # data['bank_amount'] += remaining_budget
       # total_budget = data['bank_amount'] - remaining_budget
        choice = None

    elif choice == "CURRENT":
        print(f"Your total budget for {date} is: {total_budget: .2f}EUR")
        choice = None

    elif choice == "HISTORY_WITH":
        year = int(input("Please select your year (numerically): "))
        month = int(input("Please select your month (numerically): "))
       # date = f"{year}", f"{month}"
        print(f"You`ve selected the following date: {date}")
        #for datetime in monthcalendar(year, month, date):
           #print(datetime.now())
       # while date not in calendar.monthcalendar(2025, 5):
          #  date = input("You`ve choose wrong date. Please try again: ")
        msg = f"Hello. This is your list of withdrawal funds for {date}: {withdrawal_hist}"
        print(msg)
        choice = None

    elif choice == "HISTORY_EXP":
        msg = f"Hello. This is your list of expenses for {date}: {expenses_hist}"
        print(msg)
        choice = None

    elif choice == "EXIT":
        msg = "You are leaving the app now. Goodbye."
        print(msg)
        sys.exit()

    else:
        print("No valid option selected.")
        choice = None







  #  print(f"Your current budget is {withdrawal}.")



