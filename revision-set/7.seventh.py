# Q190. Calculate a^b recursively.
def power(a,b):
    if a==0 and b<0:
        return 'Undefined'
    if b==0:
        return 1
    if b<0:
        return 1/a*power(a,b+1)
    return a*power(a,b-1)
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
result=power(a,b)
print(result)

# Q179. Write a function that takes a list and returns the most frequent element.
def most_frequent(numbers):
    if len(numbers) == 0:
        return "List is empty"
    frequency={}
    for num in numbers:
        if num not in frequency:
            frequency[num]=1
        else:
            frequency[num]+=1
    most_frequent = numbers[0]
    highest_count = frequency[numbers[0]]
    for num in frequency:
        if frequency[num]>highest_count:
            highest_count=frequency[num]
            most_frequent=num
    return most_frequent
numbers = list(map(int, input("Enter a list: ").split()))
result = most_frequent(numbers)
print(result)


# Q217. Find the first occurrence of a character recursively.
def first_occurence(text,x,index=0):
    if index==len(text):
        return -1
    if text[index]==x:
        return index
    return first_occurence(text,x,index+1)
text=input("Enter a string: ")
x=input("Entr a char: ")
result=first_occurence(text,x)
print(result)

# Q55. Find the second-largest digit in a number.
number=int(input("Enter a number: "))
largest=float('-inf')
second=float('-inf')
while number>0:
    digit=number%10
    if digit>largest:
        second=largest
        largest=digit
    elif largest>digit>second:
        second=digit
    number//=10
print(second if second!=float('-inf') else 'Not there')
    

# Q135. Function to calculate LCM.
def find_lcm(a,b):
    if a==0 or b==0:
        return 0
    else:
        larger=a if a>b else b
        for num in range(larger,a*b+1):
            if num%a==0 and num%b==0:
                return num
a=abs(int(input("Enter a number: ")))
b=abs(int(input("Enter a number: ")))
result=find_lcm(a,b)
print(result)