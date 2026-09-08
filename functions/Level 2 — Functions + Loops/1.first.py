# function to calculate factorial.
def factorial(number):
    result=1
    if number<0:
        return -1
    for i in range(1,number+1):
        result*= i
    return result
number= int(input("Enter a number: "))
result=factorial(number)
print(result)

# Function to calculate the sum from 1 to n.
def total_sum(n):
    return n*(n+1)//2                             # // produces integer division so replacing int()
number= int(input("Enter a number: "))
result=total_sum(number)
print(result)

# Function to calculate the sum of even numbers up to n.
def even_sum(n):
    k=n//2
    return k*(k+1)
number= int(input("Enter a number: "))
result=even_sum(number)
print(result)

# Function to calculate the sum of odd numbers up to n.
def odd_sum(n):
    k=(n+1)//2
    return k*k
number= int(input("Enter a number: "))
result=odd_sum(number)
print(result)

# Function to count digits.
def count_digits(number):
    number=abs(number)
    count=0
    if number==0:
        count=1
    while number>0:
        number//=10
        count+=1
    return count
number= int(input("Enter a number: "))
result=count_digits(number)
print(result)
