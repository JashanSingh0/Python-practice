# Function that accepts a list and returns its sum.
def list_sum(numbers):
    total=0
    for number in numbers:
        total+=number
    return total
numbers = list(map(int,input("Enter a number: ").split()))
result=list_sum(numbers)
print(result)

# Function that accepts a list and returns its maximum.
def list_max(numbers):
    if not numbers:
        return False
    largest=numbers[0]
    for number in numbers:
        if number>largest:
            largest=number
    return largest
numbers = list(map(int,input("Enter a number: ").split()))
result=list_max(numbers)
print(result)

# Function that accepts a list and returns its minimum.
def list_min(numbers):
    if not numbers:
        return False
    smallest=numbers[0]
    for number in numbers:
        if smallest>number:
            smallest=number
    return smallest
numbers = list(map(int,input("Enter a number: ").split()))
result=list_min(numbers)
print(result)

# Function that accepts a list and counts even numbers.
def even_count(numbers):
    count=0
    for number in numbers:
        if number%2==0:
            count+=1
    return count
numbers = list(map(int,input("Enter a number: ").split()))
result=even_count(numbers)
print(result)

# Function that accepts a list and counts odd numbers.
def odd_count(numbers):
    count=0
    for number in numbers:
        if number%2==1:
            count+=1
    return count
numbers = list(map(int,input("Enter a number: ").split()))
result=odd_count(numbers)
print(result)