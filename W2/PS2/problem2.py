'''
PROBLEM 2: PAYING DEBT OFF IN A YEAR  (15.0/15.0 points)
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180 
'''


balance = 3329
annualInterestRate = 0.2
payment = 0
new_balance = balance
while new_balance > 0:
    new_balance = balance
    for month in range (1,13):
        new_balance -= payment
        new_balance += (new_balance*(annualInterestRate/12))
    payment += 10
print('Lowest Payment: ' + str(payment-10))

