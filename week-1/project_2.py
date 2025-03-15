def calculate_compound_interest(p, r, t, n):
    """
    Calculate compound interest using the formula: a = p(1 + r/n)^(nt)
    
    Args:
        p (float): Principal amount
        r (float): Annual interest rate (as percentage)
        t (float): Time in years
        n (float): Number of times interest is compounded per year
        
    Returns:
        tuple: (final_amount, interest)
    """
    final_amount = p * (1 + r/n)**(n*t)
    interest = final_amount - p
    return final_amount, interest

try:
    # Get user input
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (%): "))
    time = float(input("Enter the time period (years): "))
    compounds = float(input("Enter number of times interest is compounded per year: "))
    
    # Calculate and display result
    amount, interest = calculate_compound_interest(principal, rate, time, compounds)
    
    print("\nResults:")
    print(f"Principal Amount: ${principal:.2f}")
    print(f"Interest Rate: {rate}%")
    print(f"Time Period: {time} years")
    print(f"Compounded {compounds} times per year")
    print(f"Final Amount: ${amount:.2f}")
    print(f"Interest Earned: ${interest:.2f}")
    
except ValueError:
    print("Please enter valid numeric values")