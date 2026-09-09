# Count odd numbers recursively.
def count_odd(numbers,index=0,count=0):
    if index==len(numbers):
        return count
    if numbers[index]%2==1:
        count+=1
    return count_odd(numbers,index+1,count)
print(count_odd([7,2,9,4,5,6]))

# Search for an element recursively.
def search_element(numbers,target,index=0):
    if index==len(numbers):
        return -1
    if numbers[index]==target:
        return index
    return search_element(numbers,target,index+1)
print(search_element([7,2,9,4,5,6],6))

# Find the first index of an element recursively.
def first_index(numbers,target,index=0):
    if index==len(numbers):
        return -1
    if numbers[index]==target:
        return index
    return first_index(numbers,target,index+1)
print(first_index([7,2,9,4,2,6],2))

# Find the last index recursively.
def last_index(numbers,target,index=None):
    if index is None:
        index=len(numbers)-1
    if index<0:
        return -1
    if numbers[index]==target:
        return index
    return last_index(numbers,target,index-1)
print(last_index([7,2,9,4,2,6],2))

# Check whether a list is sorted recursively.
def check_sort(numbers,index=1):
    if index==len(numbers):
        return True
    if numbers[index-1]<=numbers[index]:
        return check_sort(numbers,index+1)
    return False
print(check_sort([1,4,7,9]))