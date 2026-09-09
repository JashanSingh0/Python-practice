# Count a particular character recursively.
def count_character(text,char,index=0,count=0):
    if index==len(text):
        return count
    if text[index].lower() == char.lower():
        count+=1
    return count_character(text,char,index+1,count)
print(count_character("naman","m"))
print(count_character("Sherry","r"))
print()

# Find the first occurrence of a character recursively.
def first_occurrence(text,char,index=0):
    if index==len(text):
        return -1
    if text[index].lower() == char.lower():
        return index
    return first_occurrence(text,char,index+1)
print(first_occurrence("naman","m"))
print(first_occurrence("Sherry","r"))
print()

# Find the last occurrence of a character recursively.
def last_occurrence(text,char,index=None):
    if index is None:
        index=len(text)-1
    if index<0:
        return -1
    if text[index].lower() == char.lower():
        return index
    return last_occurrence(text,char,index-1)
print(last_occurrence("naman","m"))
print(last_occurrence("Sherry","r"))
print()

# Remove a character from a string recursively.
def remove_character(text,char,index=0):
    if index==len(text):
        return ""
    if char==text[index]:
        return remove_character(text,char,index+1)
    return text[index]+remove_character(text,char,index+1)
print(remove_character("naman","m"))
print(remove_character("Sherry","r"))
print()

# Replace all occurrences of a character recursively.
def replace_character(text,char,target,index=0):
    if index==len(text):
        return ""
    if char==text[index]:
        return target+replace_character(text,char,target,index+1)
    return text[index]+replace_character(text,char,target,index+1)
print(replace_character("naman","m","s"))
print(replace_character("Sherry","r","m"))
print()