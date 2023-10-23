employee_count = int (input("How many employees worked this week? "))
print()
days = [x for x in range(1, 6)]

#pay overview:
hourly_wage = 8.50
overtime_hourly_pay = 12.75

for num in range(1, employee_count + 1):
    hours = sum([int(input(f"How many hours did Employee {num} work on day {day}? ")) for day in days])
    print(f"Employee {num} worked {hours} and earned ${(hours * hourly_wage if hours <= 40 else (40 * hourly_wage + (hours - 40) * overtime_hourly_pay))} this week")