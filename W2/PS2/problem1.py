'''

PROBLEM 1: PAYING THE MINIMUM  (10.0/10.0 points)
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance, and print to screen something of the format:

Month: 1
Minimum monthly payment: 96.0
Remaining balance: 4784.0
Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135 
Finally, print out the total amount paid that year and the remaining balance at the end of the year in the format:

Total paid: 96.0
Remaining balance: 4784.0
A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

Note that the grading script looks for the order in which each value is printed out. We provide sample test cases below; we suggest you develop your code on your own machine, and make sure your code passes the sample test cases, before you paste it into the box below.
'''

mon_unpaid_balance = 0
sum = 0
for mes  in range (1,13):
    mir = annualInterestRate / 12.0
    print 'Month:', mes
    min_payment =round((monthlyPaymentRate * balance),2)
    sum += min_payment
    print "Minimum monthly payment:",  min_payment  
    mon_unpaid_balance  = balance - min_payment
    #(Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    balance = round((mon_unpaid_balance + (mir * mon_unpaid_balance)),2)
    print "Remaining balance:", balance
    
print "Total paid:",sum
print "Remaining balance:", balance
