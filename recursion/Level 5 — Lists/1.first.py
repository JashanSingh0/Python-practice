# Print every element of a list recursively.
def print_element(numbers,index=0):
    if index==len(numbers):
        return 
    print(numbers[index])
    return print_element(numbers,index+1)
print_element([1,2,3,4,5])

# Find the sum of a list recursively.
def sum_list(numbers,index=0):
    if index==len(numbers):
        return 0
    return numbers[index]+sum_list(numbers,index+1)
print(sum_list([1,2,3,4,5]))

# def sum_list(numbers,index=0,total=0):
#     if index==len(numbers):
#         return total
#     total+=numbers[index]
#     return sum_list(numbers,index+1,total)
# print(sum_list([1,2,3,4,5]))

# Find the maximum element recursively.
def largest_element(numbers,index=0):
    if index==len(numbers)-1:
        return numbers[index]
    largest=largest_element(numbers,index+1)
    if numbers[index]>largest:
        return numbers[index]
    return largest
print(largest_element([7,2,9,4,5]))

# def largest_element(numbers,index=0,largest=float("-inf")):
#     if index==len(numbers):
#         return largest
#     if numbers[index]>largest:
#         largest=numbers[index]
#     return largest_element(numbers,index+1,largest)
# print(largest_element([7,2,9,4,5]))

# Find the minimum element recursively.
def smallest_element(numbers,index=0):
    if index==len(numbers)-1:
        return numbers[index]
    smallest=smallest_element(numbers,index+1)
    if numbers[index]<smallest:
        return numbers[index]
    return smallest
print(smallest_element([7,2,9,4,5]))

# def smallest_element(numbers,index=0,smallest=float("inf")):
#     if index==len(numbers):
#         return smallest
#     if numbers[index]<smallest:
#         smallest=numbers[index]
#     return smallest_element(numbers,index+1,smallest)
# print(smallest_element([7,2,9,4,5]))


# Count even numbers recursively.
def count_even(numbers,index=0,count=0):
    if index==len(numbers):
        return count
    if numbers[index]%2==0:
        count+=1
    return count_even(numbers,index+1,count)
print(count_even([7,2,9,4,5,6]))

