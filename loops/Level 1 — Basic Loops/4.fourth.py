# Print the first n natural numbers.
n = int(input("Enter a number: "))
for num in range(1,n+1):
    print(num,end=' ')
print("\n")

# Print the first n even numbers.
n = int(input("Enter a number: "))
for num in range(1,n+1):
    print(2*num,end=' ')
print("\n")

# Print the first n odd numbers.
n = int(input("Enter a number: "))
for num in range(1,n+1):
    print(2*num-1,end=' ')
print("\n")

# Print the first n multiples of 7.
n = int(input("Enter a number: "))
for num in range(1,n+1):
    print(7*num,end=' ')