# Q206. Calculate multiplication recursively using addition.
def multiply(a,b):
    if b==0:
        return 0
    if b<0:
        return -multiply(a, -b)
    return a+multiply(a,b-1)
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
result=multiply(a,b)
print(result)

# Q40. Check whether a number is a palindrome.
n=int(input("Enter a number: "))
original_num=n
reversed_num=0
while n>0:
    digit=n%10
    reversed_num=reversed_num*10+digit
    n//=10
print(original_num==reversed_num)

# Q171. Write a function that calls another function.
def first(num):
    def second(num):
        return num*2
    result=second(num)
    return result
num=int(input("Enter a number: "))
result=first(num)
print(result)

def power(num):
    return num**2
def run_function(num):
    result=power(num)
    return result
num=int(input("Enter a number: "))
result=run_function(num)
print(result)


# Q192. Find digit sum recursively.
def digit_sum(number):
    numbers=abs(numbers)
    if number==0:
        return 0
    digit=number%10
    return digit+digit_sum(number//10)
num=int(input("Enter a number: "))
result=digit_sum(num)
print(result)

# Q160. Function that counts occurrences of an element.
def count_occurrences(numbers,x,index=0):
    if index==len(numbers):
        return 0
    if numbers[index]==x:
        return 1+count_occurrences(numbers,x,index+1)
    return count_occurrences(numbers,x,index+1)
numbers=list(map(int,input("Enter a list: ").split()))
x=int(input("Enter a number: "))
result=count_occurrences(numbers,x)
print(result)