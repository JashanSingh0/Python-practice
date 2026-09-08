# Function to calculate digit sum.
def digit_sum(number):
    number=abs(number)
    sum_of_digits=0
    while number>0:
        sum_of_digits+=number%10
        number//=10
    return sum_of_digits
number= int(input("Enter a number: "))
result=digit_sum(number)
print(result)

# Function to reverse a number.
def reverse_number(number):
    if number<0: 
        sign =-1 
    else:
        sign=1
    number=abs(number)
    reverse_num=0
    while number>0:
        digit=number%10
        reverse_num=(reverse_num*10)+digit
        number//=10
    return sign*reverse_num
number= int(input("Enter a number: "))
result=reverse_number(number)
print(result)

# Function to check palindrome number.
def check_palindrome(number):
    original=number
    number=abs(number)
    reverse_num=0
    while number>0:
        digit=number%10
        reverse_num=(reverse_num*10)+digit
        number//=10
    return reverse_num==original
number= int(input("Enter a number: "))
result=check_palindrome(number)
print(result)

# Function to check prime.
def check_prime(number):
    if number<2:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True
number= int(input("Enter a number: "))
result=check_prime(number)
print(result)

# Function to print primes up to n.
def print_primes(number):
    for i in range(2,number+1):
        is_prime=True
        for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            print(i)
number= int(input("Enter a number: "))
print_primes(number)

def print_primes(number):
    for i in range(2,number+1):
        if check_prime(i):
            print(i)
number= int(input("Enter a number: "))
print_primes(number)
