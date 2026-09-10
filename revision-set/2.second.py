# Q67. Find the LCM of two numbers.
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
if a==0 or b==0:
    print(0)
else:
    larger= a if a>b else b
    for num in range(larger,a*b+1):
        if num%a==0 and num%b==0:
            break
    print(num)


# Q213. Check whether a string is a palindrome recursively.
def check_palindrome(text):
    def rev_string(text,index=None):
        if index is None:
            index=len(text)-1
        if index<0:
            return ""
        return text[index]+rev_string(text,index-1)
    reverse=rev_string(text)
    return text==reverse
text=input("Enter a string: ")
result=check_palindrome(text)
print(result)

# Q129. Function to check prime.
def check_prime(number):
    if number<2:
        return False
    for num in range(2,number):
        if number%num==0:
            return False
    return True    
number=int(input("Enter a number: "))
result=check_prime(number)
print(result)

# Q191. Count digits recursively.
def count_digits(number,first=True):
    number=abs(number)
    if number==0:
        return 1 if first else 0
    return 1+count_digits(number//10,False)
number=int(input("Enter a number: "))
result=count_digits(number)
print(result)


# Q161. Function that finds the second-largest element.
def second_largest(numbers):
    largest=float('-inf')
    second=float('-inf')
    for num in numbers:
        if num>largest:
            second=largest
            largest=num
        elif largest>num>second:
            second=num
    return second
number=list(map(int,input("Enter a number: ").split()))
result=second_largest(number)
print(result)