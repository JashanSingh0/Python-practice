# Write a function that returns the largest of three numbers.
def larger(a,b,c):
    largest=a
    if b>largest:
        largest=b
    if c>largest:
        largest=c
    return largest
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
result=larger(a,b,c)
print(result)

# Write a function that returns the smallest of three numbers.
def smaller(a,b,c):
    smallest=a
    if b<smallest:
        smallest=b
    if c<smallest:
        smallest=c
    return smallest
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
result=smaller(a,b,c)
print(result)

# Write a function that converts Celsius to Fahrenheit.
def celsius_to_fahrenheit(c):
    return c*9/5+32
degrees=int(input("Enter degrees: "))
result=celsius_to_fahrenheit(degrees)
print(result)

# Write a function that converts Fahrenheit to Celsius.
def fahrenheit_to_celsius(f):
    return (f-32)*5/9
degrees=int(input("Enter degrees: "))
result=fahrenheit_to_celsius(degrees)
print(result)

# Write a function that calculates the area of a circle.
import math
def area(radius):
    return math.pi*radius*radius
radius=int(input("Enter radius: "))
result=area(radius)
print(result)