# Read principal, rate (% per annum) and time (years)
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (% per annum): "))
time = float(input("Enter time (in years): "))

# Amount = P x (1 + R/100)^T ; CI = Amount - P
amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print(f"Compound Interest = {compound_interest:.2f}")
print(f"Total Amount      = {amount:.2f}")