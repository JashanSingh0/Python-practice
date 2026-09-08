# Function that accepts three numbers and returns their average.
def average(a,b,c):
    return (a+b+c)/3
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
c= int(input("Enter a number: "))
result=average(a,b,c)
print(result)

# Function that accepts two numbers and returns their GCD.
def find_gcd(a,b):
    if a==0 or b==0:
        return max(a,b)
    smaller=a if a<b else b
    gcd=1
    for i in range(1,smaller+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
result=find_gcd(a,b)
print(result)

# Function that accepts two numbers and returns their LCM.
def find_lcm(a,b):
    if a == 0 or b == 0:
        return 0
    larger=a if a>b else b
    for i in range(larger,a*b+1):
        if i%a==0 and i%b==0:
            return i
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
result=find_lcm(a,b)
print(result)

# Function that accepts a number and a digit and counts that digit.
def count_digit(number,digit):
    number = abs(number)
    count=0
    if number==0 and digit==0:
        count=1
        return count
    while number>0:
        current_digit=number%10
        if current_digit==digit:
            count+=1
        number//=10
    return count
number= int(input("Enter a number: "))
digit= int(input("Enter a digit: "))
result=count_digit(number,digit)
print(result)


# Function that accepts a number and returns its reverse.
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