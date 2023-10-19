initial_investment = float(input("Enter the initial investment: £"))
target_value = float(input("Enter the target value: £"))
interest_rate = 0.10

years = 0

while initial_investment < target_value:
    initial_investment += initial_investment * interest_rate
    years += 1
    months = years * 12
    days = years * 365

print(f"It will take {years} years for the investment to grow to £{target_value}.")
print(f"It will take {months} months for the investment to grow to £{target_value}.")
print(f"It will take {days} days for the investment to grow to £{target_value}.")
