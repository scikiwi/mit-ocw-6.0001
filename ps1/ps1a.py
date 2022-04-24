total_cost = float(input("Total cost: "))
portion_saved = float(input("Portion saved: "))
annual_salary = float(input("Annual salary: "))
monthly_salary = annual_salary / 12

r = 0.04
portion_down_payment = 0.25 * total_cost
current_savings = 0

months = 0

while current_savings < total_cost * portion_down_payment:
    current_savings += monthly_salary * portion_saved + current_savings * r / 12
    months += 1
    
print(months, "months required")
