# Find the factorial of n.
n=abs(int(input("Enter a number: ")))
result=1
for num in range(1,n+1):
    result*=num
print(result)

# Calculate a^b using a loop without using **.
a=int(input("Enter a : "))
b=int(input("Enter b : "))
result=1
for i in range(b):
    result=result*a
print(result)

# Check whether a number is prime.
n=abs(int(input("Enter a number: ")))
if n<2:
    print("Not a prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not a prime")
            break
    else:
        print("Prime number")

# Print all prime numbers from 1 to n.
n=abs(int(input("Enter a number: ")))
for i in range(2,n+1):
    is_prime=True
    for div in range(2,i):
        if i%div==0:
            is_prime=False
            break
    if is_prime:
        print(i)


# Count prime numbers from 1 to n.
count=0
n=abs(int(input("Enter a number: ")))
if n==0 or n==1:
    print(count)
else:
    for i in range(2,n+1):
        is_prime=True
        for div in range(2,i):
            if i%div==0:
                is_prime=False
                break
        if is_prime:
            count+=1
    print(count)