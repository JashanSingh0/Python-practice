# Write a function that checks whether a number is even.
def is_even(number):
    return number%2==0
num=int(input("Enter a number: "))
result=is_even(num)
print(result)

# Write a function that checks whether a number is odd.
def is_odd(number):
    return number%2==1
num=int(input("Enter a number: "))
result=is_odd(num)
print(result)

# Write a function that checks whether a number is positive.
def is_positive(number):
    return number>0
num=int(input("Enter a number: "))
result=is_positive(num)
print(result)

# Write a function that checks whether a number is negative.
def is_negative(number):
    return number<0
num=int(input("Enter a number: "))
result=is_negative(num)
print(result)

# Write a function that returns the larger of two numbers.
def larger(a,b):
    if a>b:
        return a
    return b
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
result=larger(a,b)
print(result)