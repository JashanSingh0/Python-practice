# Print:
# *****
# ****
# ***
# **
# *
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print('* ',end='')
    print()

# Print:
# 1
# 22
# 333
# 4444
# 55555
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')
    print()

# Print:
# 12345
# 1234
# 123
# 12
# 1
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()


# Print a centered pyramid using numbers.
n=int(input("Enter no. of rows: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(2*i-1):
        print('*',end=' ')
    print()

# Given two nested loops, determine their Big-O time complexity.
for i in range(n):
    for j in range(n):
        print(i, j)
# Outer loop → n times
# Inner loop → n times for each outer iteration
# n × n = n²
# O(n²)