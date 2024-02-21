def calculate_profit(N):
    total_income = 100
    total_expenses = 0.7 * total_income
    total_revenue = 50 * N 
    profit = total_revenue - total_expenses
    return profit

T = int(input())
for i in range(T):
    N = int(input())
    print(calculate_profit(N))