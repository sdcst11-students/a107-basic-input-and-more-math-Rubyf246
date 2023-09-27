#!python3

# Heron's formula is a method of finding the area of a any triangle if you know the lengths of 3 sides.

'''
write a program to calculate the area of a triangle provided the 3 sides are known:
sample:
I will use Heron's formula to find the area of a triangle provided that all 3 sides are known.
You will need to enter the lengths of the 3 sides: a, b and c

Enter the length of side a: 3
Enter the length of side b: 5
Enter the length of side c: 7

Your half perimeter is 7.5
The area of your triangle is 6.495



I will use Heron's formula to find the area of a triangle provided that all 3 sides are known.
You will need to enter the lengths of the 3 sides: a, b and c

Enter the length of side a: 5
Enter the length of side b: 12
Enter the length of side c: 12

Your half perimeter is 14.5
The area of your triangle is 29.342
'''
A = int(input("Give me the number for side A , then press enter:"))
B = int(input( "Give me the number for side B, then press enter:"))
C = int (input( "Give me the number for side C, then press enter:"))
s = (A + B + C)/2
Area = (s * (s-A) * (s-B) * ( s-C)) ** (1/2)

print(f"SEMI PERIMETER: {s}")
print(f"AREA: {Area}")
