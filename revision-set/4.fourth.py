# Q233. Find the second-largest element recursively.
def second_largest(numbers,index=0,largest=float('-inf'),second=float('-inf')):
    if index== len(numbers):
        return second if second != float('-inf') else 'not there'
    if numbers[index]>largest:
        second=largest
        largest=numbers[index]
    elif largest>numbers[index]>second:
        second=numbers[index]
    return second_largest(numbers,index+1,largest,second)
numbers=list(map(int,input("Enter a list: ").split()))
result=second_largest(numbers)
print(result)

# Q126. Function to calculate digit sum.
def digit_sum(number):
    total=0
    numbers=abs(numbers)
    while number>0:
        digit=number%10
        total+=digit
        number//=10
    return total
number=int(input("Enter a number: "))
result=digit_sum(number)
print(result)

# Q163. Function that removes duplicates without using set().
def remove_duplicates(numbers):
    new_list=[]
    for num in numbers:
        if num not in new_list:
            new_list.append(num)
    return new_list
numbers=list(map(int,input("Enter a list: ").split()))
result=remove_duplicates(numbers)
print(result)

# Q201. Find nth Fibonacci number recursively.
def nth_fibonacci(n,a=0,b=1):
    if n<=0:
        return -1
    if n==1:
        return a
    return nth_fibonacci(n-1,b,a+b)
number=int(input("Enter a number: "))
result=nth_fibonacci(number)
print(result)

# Q152. Function that accepts a list and returns its maximum.
def max_element(numbers):
    largest=float('-inf')
    for num in numbers:
        if num>largest:
            largest=num
    return largest
numbers=list(map(int,input("Enter a list: ").split()))
result=max_element(numbers)
print(result)