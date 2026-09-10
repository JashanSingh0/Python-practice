# Count elements greater than x recursively.
def count_greater(numbers,x,index=0):
    if index==len(numbers):
        return 0
    if numbers[index]>x:
        return 1+count_greater(numbers,x,index+1)
    return count_greater(numbers,x,index+1)
numbers = list(map(int, input("Enter the list: ").split()))
result = count_greater(numbers,4)
print(result)

# Count elements smaller than x recursively.
def count_smaller(numbers,x,index=0):
    if index==len(numbers):
        return 0
    if numbers[index]<x:
        return 1+count_smaller(numbers,x,index+1)
    return count_smaller(numbers,x,index+1)
numbers = list(map(int, input("Enter the list: ").split()))
result = count_smaller(numbers,4)
print(result)

# Find the product of all elements recursively.
def product_elements(numbers,index=0):
    if index==len(numbers):
        return 1
    return numbers[index]*product_elements(numbers,index+1)
numbers = list(map(int, input("Enter the list: ").split()))
result = product_elements(numbers)
print(result)

# Find the number of occurrences of the maximum element recursively.
def count_largest(numbers,index=0,count=0,largest=float('-inf')):
    if index==len(numbers):
        return count
    if numbers[index]>largest:
        largest=numbers[index]
        count=1
    elif largest==numbers[index]:
        count+=1
    return count_largest(numbers,index+1,count,largest)
numbers = list(map(int, input("Enter the list: ").split()))
result = count_largest(numbers)
print(result)   

# Check whether two lists are equal recursively.
def list_equal(list1,list2,index=0):
    if len(list1)!=len(list2):
        return False
    if index==len(list1):
        return True
    if list1[index]!=list2[index]:
        return False
    return list_equal(list1,list2,index+1)
list1 = list(map(int, input("Enter 1st list: ").split()))
list2 = list(map(int, input("Enter 2nd list: ").split()))
result = list_equal(list1,list2)
print(result)   