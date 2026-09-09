# Calculate multiplication recursively using addition.
def multiply(a,b):
    if b==0:
        return a
    return a+multiply(a,b-1)
print(multiply(2,3))

# Calculate division recursively using subtraction.
def divide(a,b,count=0):
    if b==0:
        return "Cannot divide by zero"
    if a<b:
        return count,a
    return divide(a-b,b,count+1)
print(divide(22,5))
print(divide(10,0))

# Calculate a^b recursively.
def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)
print(power(2,3))

# Find the sum of squares from 1 to n recursively.
def square_sum(n):
    if n==0:
        return 0
    return n**2+square_sum(n-1)
print(square_sum(6))


# Find the sum of cubes from 1 to n recursively.
def cube_sum(n):
    if n==0:
        return 0
    return n**3+cube_sum(n-1)
print(cube_sum(6))