# Find the sum of squares from 1 to n.
result=0
n=int(input("Enter a number: "))
for num in range(1,n+1):
    result+=num*num
print(result,end='\n')

result=0
n=int(input("Enter a number: "))
result=n*(n+1)*(2*n+1)/6
print(result,end='\n')

# Find the sum of cubes from 1 to n.
result=0
n=int(input("Enter a number: "))
for num in range(1,n+1):
    result+=num**3
print(result,end='\n')

result=0
n=int(input("Enter a number: "))
result=(n*(n+1))**2
print(result,end='\n')

# Find the sum of all numbers divisible by 3 or 5.
result=0
n=int(input("Enter a number: "))
for num in range(1,n+1):
    if num%3==0 or num%5==0:
        result+=num
print(result,end='\n')

# Count how many numbers between 1 and n are divisible by 7.
count=0
n=int(input("Enter a number: "))
for num in range(1,n+1):
    if num%7==0:
        count+=1
print(count,end='\n')

count=0
n=int(input("Enter a number: "))
count=n//7
print(count,end='\n')

# Find the difference between the sum of even and odd numbers from 1 to n.
n=int(input("Enter a number: "))
k_even = n//2
k_odd =(n+1)//2
if k_even==k_odd:
    print(k_even)
else:
    print(-k_odd)