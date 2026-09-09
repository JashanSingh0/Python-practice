# Write a recursive function that prints "Hello" 5 times.
def print_hello(num):
    if num==0:
        return 
    print('Hello')
    print_hello(num-1)
print_hello(5)
print()

# Print numbers from 1 to n recursively.
def print_numbers(n):
    if n==0:
        return
    print_numbers(n-1)
    print(n)
print_numbers(5)
print()

# Print numbers from n to 1 recursively.
def print_numbers(n):
    if n==0:
        return
    print(n)
    print_numbers(n-1)
print_numbers(5)
print()

# Print even numbers from 1 to n recursively.
def print_numbers(n):
    if n==0:
        return
    print_numbers(n-1)
    if n%2==0:
        print(n)
print_numbers(15)
print()

# Print odd numbers from 1 to n recursively.
def print_numbers(n):
    if n==0:
        return
    print_numbers(n-1)
    if n%2==1:
        print(n)
print_numbers(15)
print()
