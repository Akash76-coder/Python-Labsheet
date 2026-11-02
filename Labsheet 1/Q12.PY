# Read principal, rate (% per annum) and time (years)
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (% per annum): "))
time = float(input("Enter time (in years): "))

# SI = (P x R x T) / 100
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print(f"Simple Interest = {simple_interest:.2f}")
print(f"Total Amount    = {total_amount:.2f}")