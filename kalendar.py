import calendar
from datetime import datetime

# Display a calendar and prompt user to pick a date
def pick_date():
    # Step 1: Ask for year and month
    year = int(input("Enter year (e.g. 2025): "))
    month = int(input("Enter month (1-12): "))

    # Step 2: Print the calendar for that month
    print("\n" + calendar.month(year, month))

    # Step 3: Get number of days in month
    _, num_days = calendar.monthrange(year, month)

    # Step 4: Ask user to pick a valid day
    while True:
        day = int(input(f"Pick a day (1-{num_days}): "))
        if 1 <= day <= num_days:
            break
        print("Invalid day, try again.")

    # Step 5: Construct the selected date
    selected_date = datetime(year, month, day)
    print(f"\n✅ You picked: {selected_date.strftime('%Y-%m-%d (%A)')}")

    # Optional: Call another function with the selected date
    # do_something_with(selected_date)

# Run it
pick_date()