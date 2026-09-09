# Function that returns all odd elements.
def odd_elements(numbers):
    new_list=[]
    for num in numbers:
        if num%2==1:
            new_list.append(num)
    return new_list
numbers= list(map(int,input("Enter the list: ").split()))
result=odd_elements(numbers)
print(result)

# Function that returns elements greater than x.
def elements_greater(numbers,x):
    new_list=[]
    for num in numbers:
        if num>x:
            new_list.append(num)
    return new_list
numbers= list(map(int,input("Enter the list: ").split()))
x= int(input("Enter x: "))
result=elements_greater(numbers,x)
print(result)


# Function that returns elements smaller than x.
def elements_smaller(numbers,x):
    new_list=[]
    for num in numbers:
        if num<x:
            new_list.append(num)
    return new_list
numbers= list(map(int,input("Enter the list: ").split()))
x= int(input("Enter x: "))
result=elements_smaller(numbers,x)
print(result)

# Function that finds the sum of positive elements.
def sum_positive(numbers):
    total=0
    for num in numbers:
        if num>0:
            total+=num
    return total
numbers= list(map(int,input("Enter the list: ").split()))
result=sum_positive(numbers)
print(result)

# Function that finds the sum of negative elements.
def sum_negative(numbers):
    total=0
    for num in numbers:
        if num<0:
            total+=num
    return total
numbers= list(map(int,input("Enter the list: ").split()))
result=sum_negative(numbers)
print(result)