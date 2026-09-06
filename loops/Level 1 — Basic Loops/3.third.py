# Print odd numbers from 1 to n.
n=int(input("Enter a number: "))
for num in range(1,n+1):
    if num%2==1:
      print(num,end=' ')  
print("\n")

# Print every second number from 1 to n.
n=int(input("Enter a number: "))
for num in range(1,n+1,2):
    print(num,end=' ')  
print("\n")

# Print numbers between two given numbers.
first=int(input("Enter 1st number: "))
last=int(input("Enter 2nd number: "))
for num in range(first,last+1):
   print(num,end=' ')
print("\n")

# Print all numbers divisible by both 3 and 5.
n = int(input("Enter a number: "))
for num in range(1,n+1):
   if num%3==0 and num%5==0:
      print(num,end=' ')
print("\n")

# Print all numbers divisible by either 3 or 5.
n = int(input("Enter a number: "))
for num in range(1,n+1):
   if num%3==0 or num%5==0:
      print(num,end=' ')
print("\n")