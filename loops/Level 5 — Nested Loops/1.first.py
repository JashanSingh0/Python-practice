# Print a square of * of size n.
n= int(input("Enter side: "))
for i in range(n):
    print(n*'* ')


# Print a rectangle of * with given rows and columns.
l= int(input("Enter length: "))
b= int(input("Enter width: "))
for i in range(b):
    print(l*'* ')

# Print a right triangle of *.
n= int(input("Enter side: "))
for i in range(1,n+1):
    print(i*'* ')

# Print an inverted right triangle.
n= int(input("Enter side: "))
for i in range(n,0,-1):
    print(i*'* ')

# Print a triangle containing numbers.
n= int(input("Enter side: "))
for i in range(1,n+1):
    for _ in range(i):
        print(i, end=' ')
    print()