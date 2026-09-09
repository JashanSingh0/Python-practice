# Function that finds the second-largest element.
def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')
    for num in numbers:
        if num>largest:
            second=largest
            largest=num
        elif largest>num>second:
            second=num
    return second
numbers= list(map(int,input("Enter the list: ").split()))
result=second_largest(numbers)
print(result)

# Function that finds the second-smallest element.
def second_smallest(numbers):
    smallest = float('inf')
    second = float('inf')
    for num in numbers:
        if num<smallest:
            second=smallest
            smallest=num
        elif smallest<num<second:
            second=num
    return second
numbers= list(map(int,input("Enter the list: ").split()))
result=second_smallest(numbers)
print(result)


# Function that removes duplicates without using set().
def remove_duplicates(numbers):
    new_list=[]
    for num in numbers:
        if num not in new_list:
            new_list.append(num)
    return new_list
numbers= list(map(int,input("Enter the list: ").split()))
result=remove_duplicates(numbers)
print(result)


# Function that checks whether a list is sorted.
def check_sort(numbers):
    if not numbers:
        return False
    for num in range(1,len(numbers)):
        if numbers[num-1]>numbers[num]:
            return False
    return True
numbers= list(map(int,input("Enter the list: ").split()))
result=check_sort(numbers)
print(result)

# Function that returns all even elements.
def even_elements(numbers):
    new_list=[]
    for num in numbers:
        if num%2==0:
            new_list.append(num)
    return new_list
numbers= list(map(int,input("Enter the list: ").split()))
result=even_elements(numbers)
print(result)