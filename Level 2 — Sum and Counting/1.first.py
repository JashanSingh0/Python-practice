# Find the sum of numbers from 1 to 10.
result=0
for num in range(1,11):
    result+=num
print(result,end="\n")

# Find the sum of numbers from 1 to n.
result=0
n=int(input("Enter a number: "))
for num in range(1,n+1):
    result+=num
print(result,end="\n")

# Find the sum of all even numbers from 1 to n.
result=0
n=int(input("Enter a number: "))
for num in range(1,n+1):
    if num%2==0:
        result+=num
print(result,end="\n")

result=0
n=int(input("Enter a number: "))
k=n//2                           # Count how many even numbers exist up to n              
result=k*(k+1)                   # Apply the formula
print(result,end="\n")

# Find the sum of all odd numbers from 1 to n.
result=0
n=int(input("Enter a number: "))
for num in range(1,n+1):
    if num%2==1:
        result+=num
print(result,end="\n")

result=0
n=int(input("Enter a number: "))
k=(n+1)//2                           # Count how many even numbers exist up to n              
result=k*k                           # Apply the formula
print(result,end="\n")

# Count numbers from 1 to n.
count=0
n=int(input("Enter a number: "))
for num in range(1,n+1):
    count+=1
print(count,end='\n')