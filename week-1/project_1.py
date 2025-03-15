def calculate_simple_interest(p, r, t):
    """Calculate simple interest using the formula: a = p(1 + rt/100)"""
    return p * (1 + (r * t / 100))

try:
    # Get user input
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (%): "))
    time = float(input("Enter the time period (years): "))
    
    # Calculate and display result
    amount = calculate_simple_interest(principal, rate, time)
    interest = amount - principal
    
    print("\nResults:")
    print(f"Principal Amount: ${principal:.2f}")
    print(f"Interest Rate: {rate}%")
    print(f"Time Period: {time} years")
    print(f"Total Amount: ${amount:.2f}")
    print(f"Interest Earned: ${interest:.2f}")
    
except ValueError:
    print("Please enter valid numeric values")