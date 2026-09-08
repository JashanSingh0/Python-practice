# Find all prime numbers using nested loops.
n = int(input("Enter a number: "))
for i in range(2,n+1):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i)

# Print a multiplication table from 1 to n.
n= int(input("Enter number of tables : "))
for i in range(1,n+1):
    for j in range(1,11):
        print(f'{i} × {j} = {i*j}')
    print()

# Print a square matrix of numbers from 1 to n².
n= int(input("Enter a number : "))
for start in range(1,n*n+1,n):
    for j in range (start,start+n):
        print(j,end=' ')
    print()


# Print the following pattern:
# 1
# 12
# 123
# 1234
# 12345
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()

# Print:
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    for j in range(1,i+1):
        print('* ',end='')
    print()
