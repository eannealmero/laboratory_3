# monthly salary is greater than or equal to 30,000.00
monthly_salary = float(input("Enter your monthly salary:"))
loan_amount = float(input("Enter loan amount request:"))

if monthly_salary >= 30000.00:
    if loan_amount <= 10 * monthly_salary:
        print("You are eligible for a loan.")
        
        # if eligible, ask how many months & add 10% interest increase
        months = int(input("How many months will it take for you to pay? "))
        interest = 0.10
        total_repay = loan_amount * (1 + interest)  # Calculate total loan with interest
        monthly_repay = total_repay / months
        
        print(f"Your total loan with interest is: {total_repay:.2f}")
        print(f"Your monthly payment in {months} months will be: {monthly_repay:.2f} ")
        # if not eligible, display a message with a reason to why it is not approved
    else:
        print("You are not eligible for the loan because the loan amount is beyond your monthly salary.")
else:
    print("You are not eligible for the loan because your monthly salary is below 30,000.00.")
