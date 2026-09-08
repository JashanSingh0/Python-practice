# Print multiples of 5 from 1 to 100.
for num in range(1,101):
    if num%5==0:
        print(num,end=' ')
print("\n")

# Print numbers divisible by 3 from 1 to 100.
for num in range(1,101):
    if num%3==0:
        print(num,end=' ')
print("\n")

# Print numbers from 1 to n.
n=int(input("Enter a number: "))
for num in range(1,n+1):
    print(num,end=' ')
print("\n")

# Print numbers from n to 1.
n=int(input("Enter a number: "))
for num in range(n,0,-1):
    print(num,end=' ')
print("\n")


# Print even numbers from 1 to n.
n=int(input("Enter a number: "))
for num in range(1,n+1):
    if num%2==0:
        print(num,end=' ')
print("\n")