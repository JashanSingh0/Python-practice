# Function to calculate Fibonacci.
def fibonacci(n):
    new_list=[]
    a,b=0,1
    for i in range(n):
        new_list.append(a)
        a,b=b,a+b
    return new_list
n=int(input("Enter a number: "))
result=fibonacci(n)
print(result)

# Function to return the nth Fibonacci number.
def nth_fibonacci(n):
    a,b=0,1
    for i in range(2,n+1):
        a,b=b,a+b
    return a
n=int(input("Enter a number: "))
result=nth_fibonacci(n)
print(result)

# Function to check Armstrong number.
def check_armstrong(number):
    if number == 0:
        return True
    total = 0
    count=0
    original=number
    temp=number
    while temp>0:
        temp//=10
        count+=1
    temp=original
    while temp>0:
        digit=temp%10
        total+=digit**count
        temp//=10
    return total==original
number=int(input("Enter a number: "))
result=check_armstrong(number)
print(result)

# Function to check perfect number.
def check_perfect(number):
    total=0
    if number <= 0:
        return False
    for i in range(1,number):
        if number%i==0:
            total+=i
    return total == number
number=int(input("Enter a number: "))
result=check_perfect(number)
print(result)

# Function to find the largest digit.
def largest_digit(number):
    number=abs(number)
    largest=0
    while number>0:
        digit=number%10
        if largest<digit:
            largest=digit
        number//=10
    return largest
number=int(input("Enter a number: "))
result=largest_digit(number)
print(result)