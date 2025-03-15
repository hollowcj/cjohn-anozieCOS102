def calculate_annuity(pmt, r, t, n):
    """
    Calculate annuity using the formula: a = pmt * [(1 + r/n)^(nt) - 1] / (r/n)
    
    Args:
        pmt (float): Monthly payment amount
        r (float): Annual interest rate (as percentage)
        t (float): Time in years
        n (float): Number of times interest is compounded per year
        
    Returns:
        tuple: (final_amount, total_payments)
    """
    if r == 0:
        final_amount = pmt * (t * n)
    else:
        final_amount = pmt * (((1 + r/n)**(n*t) - 1) / (r/n))
    total_payments = pmt * (t * n)
    return final_amount, total_payments

try:
    # Get user input
    payment = float(input("Enter the monthly payment amount: "))
    rate = float(input("Enter the annual interest rate (%): "))
    time = float(input("Enter the time period (years): "))
    compounds = float(input("Enter number of times interest is compounded per year: "))
    
    # Calculate and display result
    amount, payments = calculate_annuity(payment, rate, time, compounds)
    
    print("\nResults:")
    print(f"Monthly Payment: ${payment:.2f}")
    print(f"Interest Rate: {rate}%")
    print(f"Time Period: {time} years")
    print(f"Compounded {compounds} times per year")
    print(f"Total Payments Made: ${payments:.2f}")
    print(f"Future Value: ${amount:.2f}")
    
except ValueError:
    print("Please enter valid numeric values")