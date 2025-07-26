"""Project: 2
You decide to host your application on servers running in the cloud.
You pick a hosting provider that charges $0.51 per hour.
You will launch your service using one server and want to know how much it will cost to operate per day, per week, per month.
Write a Python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How many days can I operate one server with $918?"""

hourly_rate = 0.51
cost_per_day = hourly_rate * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30  

budget = 918
days_operable = budget / cost_per_day


print(f"💰 Cost to operate one server:")
print(f"Per Day  : ${cost_per_day:.2f}")
print(f"Per Week : ${cost_per_week:.2f}")
print(f"Per Month: ${cost_per_month:.2f}\n")

print(f"📅 With ${budget}, you can operate one server for approximately {days_operable:.2f} days.")
