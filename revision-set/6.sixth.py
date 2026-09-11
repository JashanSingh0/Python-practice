# Q66. Find the GCD of two numbers using a loop.
a=abs(int(input("Enter a number: ")))
b=abs(int(input("Enter a number: ")))
if a == 0:
    gcd=b
elif b == 0:
    gcd=a
else:
    smaller=a if a<b else b
    for num in range(smaller,0,-1):
        if a%num==0 and b%num==0:
            gcd=num
            break
print(gcd)

# Q231. Reverse a list recursively.
def reverse_list(numbers,index=None,new_list=None):
    if new_list is None:
        new_list=[]
    if index is None:
        index=len(numbers)-1
    if index<0:
        return new_list
    new_list.append(numbers[index])
    return reverse_list(numbers,index-1,new_list)
numbers=list(map(int,input("Enter a list: ").split()))
result=reverse_list(numbers)
print(result)

# Q128. Function to check palindrome number.
def check_palindrome(number):
    if number<0 or (number%10==0 and number!=0):
        return False
    else:
        reverse=0
        while number>reverse:
            digit=number%10
            reverse=reverse*10+digit
            number//=10
        return number==reverse or number==reverse//10
number=int(input("Enter a number: "))
result=check_palindrome(number)
print(result)

# Q74. Check whether a number is an Armstrong number.
number=int(input("Enter a number: "))
original=number
temp=number
power=0
total=0
while temp>0:
    temp//=10
    power+=1
temp=original
while temp>0:
    digit=temp%10
    total+=digit**power
    temp//=10
print(original==total)


# Q159. Function that returns the index of an element.
def find_index(numbers,x,index=0):
    if index==len(numbers):
        return -1
    if numbers[index]==x:
        return index
    return find_index(numbers,x,index+1)
numbers=list(map(int,input("Enter a list: ").split()))
x=int(input("Enter a number: "))
result=find_index(numbers,x)
print(result)