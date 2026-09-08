# Function that accepts a list and returns the average.
def list_avg(numbers):
    if not numbers:
        return False
    total=0
    for num in numbers:
        total+=num
    return total/len(numbers)
numbers = list(map(int,input("Enter a number: ").split()))
result=list_avg(numbers)
print(result)

# Function that accepts a list and reverses it without reverse().
def list_rev(numbers):
    if not numbers:
        return False
    new_list=[]
    for num in range(len(numbers)-1,-1,-1):
        new_list.append(numbers[num])
    return new_list
numbers = list(map(int,input("Enter a number: ").split()))
result=list_rev(numbers)
print(result)

# Function that searches for an element in a list.
def list_search(numbers,element):
    for num in numbers:
        if num==element:
            return True
    return False
numbers = list(map(int,input("Enter a number: ").split()))
element=int(input("Enter a number: "))
result=list_search(numbers,element)
print(result)

# Function that returns the index of an element.
def list_index(numbers,element):
    for num in range(len(numbers)):
        if element==numbers[num]:
            return num
    return -1
numbers = list(map(int,input("Enter a number: ").split()))
element=int(input("Enter a number: "))
result=list_index(numbers,element)
print(result)

# Function that counts occurrences of an element.
def list_count(numbers,element):
    count=0
    for num in numbers:
        if element==num:
            count+=1
    return count
numbers = list(map(int,input("Enter a number: ").split()))
element=int(input("Enter a number: "))
result=list_count(numbers,element)
print(result)