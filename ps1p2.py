##Problem Set 1, Problem 2
##Name: CRossi
##Program to calculate the minimum fixed monthly payments
##needed in order to pay off a credit card balance within 12 months
original_Balance = float(raw_input('Enter the outstanding balance on your credit card: '))
annual_Interest_Rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
monthly_Interest_Rate = annual_Interest_Rate/12.0
number_Of_Months = 13
minimum_Monthly_Payment = 10
remaining_Balance = original_Balance

while remaining_Balance > 0:
    number_Of_Months = 0;
    remaining_Balance = original_Balance
    minimum_Monthly_Payment +=10

    for i in range(1, 13):
        remaining_Balance = (remaining_Balance * (1.0 + monthly_Interest_Rate) - minimum_Monthly_Payment)
        number_Of_Months +=1
        if remaining_Balance < 0:
            break
        


print 'RESULT\n', 'Monthly payment to pay off debt in 1 year:', minimum_Monthly_Payment, '\n', 'Number of months needed:', number_Of_Months, '\n', 'Balance:', round(remaining_Balance, 2)

                              
