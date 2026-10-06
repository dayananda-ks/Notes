#  Bank loan eligibility and EMI planner: Accept age, monthly income, credit score, and loan amount.
#  Reject if age is outside 21-58, income is below Rs.15,000, or the credit score is below 650.
#  Set the interest rate by credit score band (650-700, 701-750,750+) and by loan amount slab. 
#  Use a loop to find the shortest tenure (in years, up to 20) where the EMI stays under 40% of income.
#  If none exists, print the reason for rejection.

name = input("Enter the name : ")
age = int(input("Enter the age : "))
monthly_income = float(input("Enter the monthly salary : "))
credit_score = int(input("Enter the credit score : "))
loan_amount = float(input("Enter the loan amount : "))
if (age <= 58) and (age >= 21):
    if (monthly_income > 15000):
        if (credit_score >= 650):
            if (credit_score >= 750):
                if (loan_amount >= 50000):
                    rate = 0.08
                else:
                    rate = 0.085
            elif (credit_score >= 701):
                if (loan_amount >= 50000):
                    rate = 0.09
                else:
                    rate = 0.095
            else:
                if (loan_amount >= 50000):
                    rate = 0.10
                else:
                    rate = 0.105
            max_emi = monthly_income * 0.40
            r = rate / 12
            found = False
            for year in range(1, 21):
                n = year * 12
                emi = (loan_amount * r * (1 + r)**n) / ((1 + r)**n - 1) #  formula take by google
                if emi <= max_emi:
                    print("Loan Approved")
                    print("Shortest Tenure:", year, "years")
                    print("Monthly EMI", round(emi, 2))
                    found = True
                    break
            if found == False:
                print("Rejected")
        else:
            print("Less credit score")
    else:
        print("Less monthly income")
else:
    print("age is not enough")
