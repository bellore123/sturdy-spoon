basic = float(input("Enter basic salary: "))

hra = basic * 0.20
da = basic * 0.10
gross_salary = basic + hra + da
tax = gross_salary * 0.05
net_salary = gross_salary - tax

print("Net Salary:", net_salary)