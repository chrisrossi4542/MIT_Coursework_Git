##Problem Set 1, Problem 1
##Name: CRossi
##Program to calculate credit card balance after one year if a person only pays
##the minimum monthly payment required by the credit card company each month

initial_Outstanding_Balance = float(raw_input('Enter the outstanding balance on your credit card: '))
annual_Interest_Rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
minimum_Monthly_Payment_Rate = float(raw_input('Enter the minimum monthly payment rate as a decimal: '))
remaining_Balance = initial_Outstanding_Balance
total_Paid = 0
monthly_Interest_Rate = annual_Interest_Rate/12.0


for i in range(1,13):
    minimum_Monthly_Payment = round((minimum_Monthly_Payment_Rate * remaining_Balance), 2)
    interest_Paid = round(((monthly_Interest_Rate) * remaining_Balance), 2)
    principal_Paid = round((minimum_Monthly_Payment - interest_Paid), 2)
    remaining_Balance = round((remaining_Balance - principal_Paid), 2)
    total_Paid = total_Paid + minimum_Monthly_Payment

    print 'Month: ', i, '\n', 'Minimum monthly payment: ', '$'+ str(minimum_Monthly_Payment), '\n', 'Principal paid: ', '$'+ str(principal_Paid),'\n', 'Remaining balance: ','$'+ str(remaining_Balance) 
   
print 'RESULT', '\n', 'Total amount paid: ', '$'+str(total_Paid), '\n', 'Remaining balance: ', '$'+ str(remaining_Balance)

