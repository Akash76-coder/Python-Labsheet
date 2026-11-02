# Read loan details
principal = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = float(input("Enter loan tenure (in years): "))

# Convert to monthly rate and number of months
monthly_rate = annual_rate / (12 * 100)
months = years * 12

if monthly_rate == 0:
    # No interest: simply divide the principal equally
    emi = principal / months
else:
    # EMI = P x r x (1+r)^n / ((1+r)^n - 1)
    factor = (1 + monthly_rate) ** months
    emi = principal * monthly_rate * factor / (factor - 1)

print(f"Monthly EMI        = {emi:.2f}")
print(f"Total payment      = {emi * months:.2f}")
print(f"Total interest     = {emi * months - principal:.2f}")