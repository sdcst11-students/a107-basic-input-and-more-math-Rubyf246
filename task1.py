'''
##### Task 1 Percent Error
Ask the user to input the following:
* the expected number
* the actual result
Calculate the percent difference between the two results. Round your answer to 2 decimal places

```
https://www.skillsyouneed.com/num/percent-change.html

Sample Output:
Enter expected: 10
Enter actual : 9
The percent difference is -10.0%

Enter expected: 12
Enter actual : 14
The percent difference is 16.67%
```
'''


a = "Give me the expected number, then press enter."
answerF = input(a)
c = "Give me the actual number, then press enter and see the result"
answerT = input (c)
Fanswer = int(answerF)
Tanswer = int(answerT)
increase = Tanswer - Fanswer
equation = increase / Fanswer * 100
x = round(equation , 2)
print(f"x: {x}")

