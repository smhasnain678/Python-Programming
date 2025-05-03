P = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan duration (years): "))
r = (annual_rate / 100) / 12
n = years * 12
EMI = (P * r * (1 + r) ** n) / ((1 + r) ** n - 1)
print("Monthly EMI:", round(EMI, 2))