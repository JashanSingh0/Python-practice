# # Write a function that returns the largest element and use it to find the second largest.
# def largest_element(numbers):
#     largest=float('-inf')
#     for num in numbers:
#         if num>largest:
#             largest= num
#     return largest
# def second_largest(numbers):
#     second=float('-inf')
#     largest=largest_element(numbers)
#     for num in numbers:
#        if largest>num>second:
#            second=num
#     return second
# number= list(map(int,input("Enter a number: ").split()))
# result=second_largest(number)
# print(result)

# # Write a function that returns whether a string is a palindrome.
# def check_palindrome(text):
#     reverse_str=''
#     for char in text:
#         reverse_str = char+reverse_str
#     return reverse_str==text
# text=input("Enter string: ")
# result=check_palindrome(text)
# print(result)

# # Write a function that returns the frequency of each character.
# def frequency_char(text):
#     frequency_map = {}
#     for char in text:
#         if char in frequency_map:
#             frequency_map[char]+=1
#         else:
#             frequency_map[char]=1
#     return frequency_map
# text=input("Enter string: ")
# result=frequency_char(text)
# print(result)


# # Write a function that takes a list and returns the most frequent element.
# def frequency_element(number):
#     frequency_map = {}
#     highest_count=0
#     for num in number:
#         if num in frequency_map:
#             frequency_map[num]+=1
#         else:
#             frequency_map[num]=1
#     for char,count in frequency_map.items():
#         if count>highest_count:
#             most_frequent=char
#             highest_count=count
#     return most_frequent
# number= list(map(int,input("Enter a number: ").split()))
# result=frequency_element(number)
# print(result)

# Write a function that combines two lists into one without duplicates.
def combine_list(list1,list2):
    new_list=[]
    for num in list1:
        if num not in new_list:
            new_list.append(num)
    for num in list2:
        if num not in new_list:
            new_list.append(num)
    return new_list
list1= list(map(int,input("Enter list 1: ").split()))
list2= list(map(int,input("Enter list 2: ").split()))
result=combine_list(list1,list2)
print(result)