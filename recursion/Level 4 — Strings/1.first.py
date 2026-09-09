# # Print every character of a string recursively.
def print_char(text, index=0):
    if index == len(text):
        return
    print(text[index])
    print_char(text, index + 1)
print_char("Sherry")
print()
 
# def print_char(text):
#     if not text:
#         return
#     print(text[0])
#     return print_char(text[1:])
# print_char("Sherry")

# Print a string in reverse recursively.
def reverse_string(text, index=None):
    if index is None:
        index=len(text)-1
    if index<0:
        return
    print(text[index])
    reverse_string(text, index - 1)
reverse_string("Sherry")
print()

# def print_rev_char(text):
#     if not text:
#         return
#     print(text[-1])
#     return print_rev_char(text[:-1])
# print_rev_char("Sherry")

# Check whether a string is a palindrome recursively.
def check_palindrome(text):
    def reverse_string(text, index=None):
        if index is None:
            index=len(text)-1
        if index<0:
            return ""
        return text[index]+reverse_string(text, index - 1)
    return text==reverse_string(text)
print(check_palindrome("naman"))
print(check_palindrome("harry"))
print()

# Count vowels recursively.
def count_vowels(text,index=0,count=0):
    if index==len(text):
        return count
    if text[index].lower() in "aeiou":
        count+=1
    return count_vowels(text,index+1,count)
print(count_vowels("naman"))
print(count_vowels("Sherry"))
print()

# Count consonants recursively.
def count_consonants(text,index=0,count=0):
    if index==len(text):
        return count
    char = text[index].lower()
    if char.isalpha() and char not in "aeiou":
        count+=1
    return count_consonants(text,index+1,count)
print(count_consonants("naman"))
print(count_consonants("Sherry"))