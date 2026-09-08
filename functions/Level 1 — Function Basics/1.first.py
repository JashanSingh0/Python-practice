# Write a function that prints "Hello World".
def hello_world():
    print("Hello World")
hello_world()

# Write a function that prints numbers from 1 to 10.
def print_numbers():
    for i in range(1,11):
        print(i)
print_numbers()

# Write a function that takes a number and prints it.
def print_number(number):
    print(number)
print_number(4)

# Write a function that takes two numbers and prints their sum.
def add(a,b):
    print(a+b)
add(4,5)

# Write a function that returns the sum of two numbers.
def add(a,b):
    return a+b
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
result= add(a,b)
print(result)