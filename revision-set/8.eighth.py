# Q222. Find the sum of a list recursively.
def total_sum(numbers,index=0):
    if index==len(numbers):
        return 0
    return numbers[index]+total_sum(numbers,index+1)
numbers=list(map(int,input("Enter a list: ").split()))
result=total_sum(numbers)
print(result)

# Q41. Find the largest digit in a number.
number=abs(int(input("Enter a number: ")))
largest=float('-inf')
if number==0:
    largest=0
while number>0:
    digit=number%10
    if digit>largest:
        largest=digit
    number//=10
print(largest)

# Q203. Check whether a number is Fibonacci recursively.
def check_fibonacci(number,a=0,b=1):
    if a>number:
        return False
    if a==number:
        return True
    return check_fibonacci(number,b,a+b)
number=int(input("Enter a number: "))
result=check_fibonacci(number)
print(result)

# Q176. Write a function that returns the largest element and use it to find the second largest.
def second_largest(numbers):
    second=float('-inf')
    def largest_element(numbers):
        largest=float('-inf')
        for num in numbers:
            if num>largest:
                largest=num
        return largest
    largest=largest_element(numbers)
    for num in numbers:
        if largest>num>second:
            second=num
    return second if second!=float('-inf') else 'Not there'
numbers= list(map(int,input("Enter a list: ").split()))
result=second_largest(numbers)
print(result)

# Q127. Function to reverse a number.
def reverse_number(number):
    sign=-1 if number<0 else 1
    number=abs(number)
    reverse=0
    while number>0:
        digit=number%10
        reverse=reverse*10+digit
        number//=10
    return sign*reverse
numbers= int(input("Enter a number: "))
result=reverse_number(numbers)
print(result)