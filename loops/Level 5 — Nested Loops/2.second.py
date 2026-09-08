# Print an inverted number triangle.
n= int(input("Enter side: "))
for i in range(n,0,-1):
    for _ in range(i):
        print(i,end=' ')
    print()

# Print a pyramid of *.
n= int(input("Enter no. of rows: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(2*i-1):
        print('*',end=' ')
    print()



# Print an inverted pyramid.
n= int(input("Enter no. of rows: "))
for i in range(n,0,-1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(2*i-1):
        print('*',end=' ')
    print()

# Print a multiplication table using nested loops.
n= int(input("Enter number of tables : "))
for i in range(1,n+1):
    for j in range(1,11):
        print(f'{i} × {j} = {i*j}')
    print()

# Print all pairs (i, j) where 1 <= i,j <= n.
n= int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f'({i},{j})')