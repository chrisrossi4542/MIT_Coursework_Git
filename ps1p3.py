##Problem Set 1, Problem 2
##Name: CRossi
##Program to calculate the minimum fixed monthly payments
##needed in order to pay off a credit card balance within 12 months
original_Balance = float(raw_input('Enter the outstanding balance on your credit card: '))
annual_Interest_Rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
monthly_Interest_Rate = annual_Interest_Rate/12.0
number_Of_Months = 13
remaining_Balance = original_Balance
monthly_Payment_Lower_Bound = original_Balance / 12.0
print 'Lower Bound is', monthly_Payment_Lower_Bound
monthly_Payment_Upper_Bound = (original_Balance * (1 + monthly_Interest_Rate)**12)/12.0
print 'Upper Bound is', monthly_Payment_Upper_Bound
minimum_Monthly_Payment = (monthly_Payment_Upper_Bound + monthly_Payment_Lower_Bound)/2.0
print 'initial min monthly payment is', minimum_Monthly_Payment
epsilon =.1


while (abs(monthly_Payment_Upper_Bound - monthly_Payment_Lower_Bound) > epsilon):
#while  abs(((minimum_Monthly_Payment*number_Of_Months) + remaining_Balance) - (original_Balance* (1 + monthly_Interest_Rate)**12)) > epsilon and minimum_Monthly_Payment < ((original_Balance * (1 + monthly_Interest_Rate)**12)/12):
#for j in range(30):
    #print 'in the upper loop, current upper bound', monthly_Payment_Upper_Bound, 'current lower bound', monthly_Payment_Lower_Bound, 'monthly payment is', minimum_Monthly_Payment
    number_Of_Months = 0;
    remaining_Balance = original_Balance

    for i in range(1, 13):
        remaining_Balance = (remaining_Balance * (1.0 + monthly_Interest_Rate) - round(minimum_Monthly_Payment, 2))
        number_Of_Months +=1
        #print 'we got to the lower loop'
        if remaining_Balance < 0:
            
            break

    if (remaining_Balance > 0):
        monthly_Payment_Lower_Bound = minimum_Monthly_Payment
    else:
        monthly_Payment_Upper_Bound = minimum_Monthly_Payment
        
    minimum_Monthly_Payment = (monthly_Payment_Upper_Bound + monthly_Payment_Lower_Bound)/2.0




print 'RESULT\n', 'Monthly payment to pay off debt in 1 year:', round(minimum_Monthly_Payment,2), '\n', 'Number of months needed:', number_Of_Months, '\n', 'Balance:', round(remaining_Balance, 2)

                              
