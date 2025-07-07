#get the monthly income 



monthly_income = float(input("Enter your monthly income: "))
monthly_expences = float(input("Enter your total monthly expenses:  "))

monthly_saving  = monthly_income - monthly_expences

print(f"Your monthly savings are  : {int(monthly_saving)}")


projected_savings = monthly_saving * 12 + ( monthly_saving * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: {int(projected_savings)}.")