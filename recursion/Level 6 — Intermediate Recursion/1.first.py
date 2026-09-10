# Reverse a list recursively.
def reverse_list(numbers, index=0):
    if index == len(numbers):
        return []
    return reverse_list(numbers, index + 1) + [numbers[index]]
numbers = list(map(int, input("Enter the list: ").split()))
result = reverse_list(numbers)
print(result)

# def reverse_list(numbers,index=None,new_list=None):
#     if new_list is None:
#         new_list = []
#     if index==None:
#         index=len(numbers)-1
#     if index<0:
#         return new_list
#     new_list.append(numbers[index])
#     return reverse_list(numbers,index-1,new_list)
# numbers= list(map(int,input("Enter the list: ").split()))
# result=reverse_list(numbers)
# print(result)

# Remove duplicates recursively.
def remove_duplicates(numbers,index=0):
    if index==len(numbers):
        return []
    new_list=remove_duplicates(numbers,index+1)
    if numbers[index] in new_list:
        return new_list
    return [numbers[index]]+new_list
numbers = list(map(int, input("Enter the list: ").split()))
result = remove_duplicates(numbers)
print(result)

# def remove_duplicates(numbers, index=0,new_list=None):
#     if new_list is None:
#         new_list = []
#     if index == len(numbers):
#         return new_list
#     if numbers[index] not in new_list:
#         new_list.append(numbers[index])
#     return remove_duplicates(numbers, index + 1,new_list)
# numbers = list(map(int, input("Enter the list: ").split()))
# result = remove_duplicates(numbers)
# print(result)


# Find the second-largest element recursively.
def second_largest(numbers,index=0,largest=float('-inf'),second=float('-inf')):
    if index==len(numbers):
        return second
    if numbers[index]>largest:
        second=largest
        largest=numbers[index]
    elif largest>numbers[index]>second:
        second=numbers[index]
    return second_largest(numbers,index+1,largest,second)
numbers = list(map(int, input("Enter the list: ").split()))
result = second_largest(numbers)
print(result)   

# Find the sum of elements at even indices recursively.
def sum_even_indices(numbers,index=0):
    if index>=len(numbers):
        return 0
    return numbers[index]+sum_even_indices(numbers,index+2)
numbers = list(map(int, input("Enter the list: ").split()))
result = sum_even_indices(numbers)
print(result) 

# Find the sum of elements at odd indices recursively.
def sum_odd_indices(numbers,index=1):
    if index>=len(numbers):
        return 0
    return numbers[index]+sum_odd_indices(numbers,index+2)
numbers = list(map(int, input("Enter the list: ").split()))
result = sum_odd_indices(numbers)
print(result)