count=0
n=int(input("Enter a number: "))
for num in range(1,n+1):
    if num%2==0:
        count+=1
print(count,end='\n')

# Count odd numbers from 1 to n.
count=0
n=int(input("Enter a number: "))
for num in range(1,n+1):
    if num%2==1:
        count+=1
print(count,end='\n')

# Count numbers divisible by 3 between 1 and n.
count=0
n=int(input("Enter a number: "))
for num in range(1,n+1):
    if num%3==0:
        count+=1
print(count,end='\n')

# Find the sum of multiples of 5 from 1 to n.
result=0
n=int(input("Enter a number: "))
for num in range(1,n+1):
    if num%5==0:
        result+=num
print(result,end='\n')

# Find the average of numbers from 1 to n.
result=0
n=int(input("Enter a number: "))
result=(n+1)/2
print(result,end='\n')
