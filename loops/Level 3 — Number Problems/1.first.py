# Count the number of digits in an integer.
count=0
n=abs(int(input("Enter a number: ")))
if n==0:
    count=1
else:
    while n>0:
        count+=1
        n=n//10
print(count,end='\n')

import math
n=abs(int(input("Enter a number: ")))
if n==0:
    count=1
else:
    count = int(math.log10(n)) +1
print(count,end='\n')

# Find the sum of digits of a number.
result=0
n=abs(int(input("Enter a number: ")))
while n>0:
    result+=n%10
    n=n//10
print(result)

# Find the product of digits of a number.
result=1
n=abs(int(input("Enter a number: ")))
if n==0:
    result=0
else:
    while n>0:
        result=result*(n%10)
        n=n//10
print(result)

# Reverse a number using a loop.
n=int(input("Enter a number: "))
sign = -1 if n<0 else 1
n=abs(n)
reversed_num=0
while n>0:
    last_digit=n%10
    reversed_num=(reversed_num*10)+last_digit
    n=n//10
reversed_num*=sign
print(reversed_num)


# Check whether a number is a palindrome.
n=int(input("Enter a number: "))
original_num=n
reversed_num=0
if n<0:
    print(False)
else:
    while n>0:
        last_digit=n%10
        reversed_num=(reversed_num*10)+last_digit
        n=n//10
print(original_num == reversed_num)