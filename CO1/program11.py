#  Find biggest of 3 numbers entered.

print("enter 3 numbers:")
a = float(input())
b = float(input())
c = float(input())
if a > b and a > c:
    print("largest number is :", a)
elif b > a and b > c:
    print("largest number is :", b)
else:
    print("largest number is :", c)