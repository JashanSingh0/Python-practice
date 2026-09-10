# Q59. Print all prime numbers from 1 to n.
n=int(input("Enter a range: "))
for i in range(2,n+1):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i)

# Q218. Find the last occurrence of a character recursively.
def last_occurence(text,x,index=None):
    if index is None:
        index=len(text)-1
    if index<0:
        return
    if text[index]==x:
        return index
    return last_occurence(text,x,index-1)
text=input("Enter a string: ")
x=input("Enter a character: ")
result=last_occurence(text,x)
print(result)

# Q178. Write a function that returns the frequency of each character.
def frequency(text,x):
    count=0
    for char in text:
        if char==x:
            count+=1
    return count
text=input("Enter a string: ")
x=input("Enter a character: ")
result=frequency(text,x)
print(result)

# Q72. Find the nth Fibonacci number using a loop.
n=int(input("Enter a number: "))
a,b=0,1
for i in range(1,n):
    a,b=b,a+b
print(a)


# Q39. Reverse a number using a loop.
number=int(input("Enter a number: "))
reversed_num=0
sign=-1 if number<0 else 1
number=abs(number)
while number>0:
    digit=number%10
    reversed_num=reversed_num*10+digit
    number//=10
print(sign*reversed_num)