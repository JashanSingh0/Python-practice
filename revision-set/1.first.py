# Q204. Calculate GCD recursively.
def find_gcd(a,b):
    if b==0:
        return a
    return find_gcd(b,a%b)
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
result=find_gcd(a,b)
print(result)

# Q157. Function that accepts a list and reverses it without reverse().
def reverse_list(numbers):
    if not numbers:
        return []
    new_list=[]
    for num in range(len(numbers)-1,-1,-1):
        new_list.append(numbers[num])
    return new_list
numbers=list(map(int,input("Enter a number: ").split()))
result=reverse_list(numbers)
print(result)

# Q37. Find the sum of digits of a number.
numbers=int(input("Enter a number: "))
total=0
while numbers>0:
    digit=numbers%10
    total+=digit
    numbers//=10
print(total)


# Q172. Write a function that accepts another function as an argument.
def run_function(function):
    return function(5,15)
def multiply(a,b):
    return a*b
def add(a,b):
    return a+b
print(run_function(multiply))
print(run_function(add))
    

# Q223. Find the maximum element recursively.
def max_element(numbers,index=0):
    if index==len(numbers)-1:
        return numbers[index]
    largest=max_element(numbers,index+1)
    if numbers[index]>largest:
        return numbers[index]
    return largest
numbers=list(map(int,input("Enter a number: ").split()))
result=max_element(numbers)
print(result)
