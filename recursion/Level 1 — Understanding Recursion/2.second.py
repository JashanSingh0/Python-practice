# Find the sum from 1 to n recursively.
def total_sum(n):
    if n==0:
        return 0
    return n+total_sum(n-1)
print(total_sum(5))

# Find the sum of even numbers recursively.
def even_sum(n):
    if n==0:
        return 0
    if n%2==0:
        return n+even_sum(n-1)
    return even_sum(n-1)
print(even_sum(15))

# Find the sum of odd numbers recursively.
def odd_sum(n):
    if n==0:
        return 0
    if n%2==1:
        return n+odd_sum(n-1)
    return odd_sum(n-1)
print(odd_sum(15))

# Calculate factorial recursively.
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))

# Calculate a^b recursively.
# Q190. Calculate a^b recursively.
def power(a,b):
    if a==0 and b<0:
        return 'Undefined'
    if b==0:
        return 1
    if b<0:
        return 1/a*power(a,b+1)
    return a*power(a,b-1)
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
result=power(a,b)
print(result)