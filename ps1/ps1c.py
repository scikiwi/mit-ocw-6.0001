annual_salary = float(input("Enter your annual salary: "))
monthly_salary = annual_salary / 12

r = 0.04
semi_annual_raise = 0.07
total_cost = 1000000
portion_down_payment = 0.25 * total_cost

high = 10000
low = 0
steps = 0

# calculates savings given monthly salary, portion saved (out of 10000), rate of return and semi annual raise
def savings(m_salary, mid, r, semi_annual_raise):
    savings = 0
    for months in range(36):
        savings += m_salary * (mid / 10000) + savings * r / 12
        if months % 6 == 0:
            m_salary += m_salary * semi_annual_raise
    return savings

if savings(monthly_salary, high, r, semi_annual_raise) < portion_down_payment - 100: # calculates upper bound for savings (assuming all monthly income is saved)
    print("It is not possible to pay the down payment in three years.")
else:
    while True:
        mid = ((high + low) // 2)
        
        current_savings = savings(monthly_salary, mid, r, semi_annual_raise)
        
        if current_savings > portion_down_payment + 100:
            high = mid
            steps += 1
        elif current_savings < portion_down_payment - 100:
            low = mid
            steps += 1
        else:
            print("Best savings rate:", mid / 10000)
            print("Steps in bisection search:", steps)
            break
