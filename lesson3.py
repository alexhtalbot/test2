money_start=float(input("How much money do you have?: $"))
saving_years=int(input("How many years do you want to save?: "))
interest_rate=float(input("What is your annual interest rate?:(%): ")) / 100

money_end=money_start*(1+interest_rate)**saving_years 

print(f"After {saving_years} years, you will have ${money_end:.2f}")

cost_of_holiday=2000
afford_holiday=money_end>=cost_of_holiday
print(f"You can afford the holiday: {afford_holiday}")
