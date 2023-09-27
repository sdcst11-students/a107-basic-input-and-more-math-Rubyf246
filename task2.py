'''
##### Task 2 Compound Interest
Ask the user to enter the following:
* The principal (amount invested or borrowed)
* The annual interest rate (expressed as a percent)
* The number of compounding periods per year
* The length of time for the investment
Calculate the final amoutn as well as the amount of interest earned. Round your answer to 2 decimal places

```
https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php
Enter the Princial: 2000
Enter the annual interest rate as a percent: 4
Enter the number of compounding periods: 4
How long is the investment period in years: 3
Your final amount is $2253.65
You earned $253.65 interest

Enter the Princial: 25000
Enter the annual interest rate as a percent: 7.5
Enter the number of compounding periods: 12
How long is the investment period in years: 6
Your final amount is $39152.94
You earned $14152.94 interest
```
'''
Principal = int(input("Give me principal number, then press enter:"))
Intrate = int(input( "Give the the percentage of your interest rate:"))
Compperyear = int (input( "Give me the number of compounding periods per year:"))
Time = int (input ("Give me the time for the inveestment:")) 
PIntrate = Intrate / 100
equation = Principal*(1 + PIntrate/Compperyear) ** (Compperyear * Time)
Final_amount = round(equation , 2)
Earned = Final_amount - Principal 
Searned = round(Earned , 2)
print(f"Final amount: {Final_amount}")
print(f"Earned: {Searned}")

