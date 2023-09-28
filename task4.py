#!python3

"""
Write a program to ask the user to input a length in centimeters. Convert this into feet and inches.  Round your inches to the nearest whole inch.
You will likely need to make use of at least one of the following:
* % modulus
* math.floor()

Sample output:
```
Enter a length in centimeters: 172
172 centimeters is 5 feet and 8 inches

Enter a length in centimeters: 32
32 centimeters is 1 feet and 1 inches
```
"""
Length = int(input("Give me the length number in centimeters, then press enter:"))
inches = Length/ 2.54 
feet = Length/  30.48
print(f"Inches: {inches}")
print(f"Feets: {feet}")
