# Function that accepts two numbers and returns the larger.
def larger(a,b):
    if a>b:
        return a
    return b
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
result=larger(a,b)
print(result)

# Function that accepts three numbers and returns the middle value.
def middle_value(a,b,c):
    if (a <= b <= c) or (c <= b <= a):
        return b
    elif (b <= a <= c) or (c <= a <= b):
        return a
    else:
        return c
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
c= int(input("Enter a number: "))
result=middle_value(a,b,c)
print(result)

# Function that accepts a range and returns its sum.
def total_sum(start,end):
    n=end-start +1
    return n*(start+end)//2
start= int(input("Enter a number: "))
end= int(input("Enter a number: "))
result=total_sum(start,end)
print(result)

# Function that accepts a range and returns the number of even values.
def total_even(start,end):
    count=0
    for i in range(start,end+1):
        if i%2==0:
            count+=1
    return count
start= int(input("Enter a number: "))
end= int(input("Enter a number: "))
result=total_even(start,end)
print(result)

# Function that accepts a range and returns the number of prime numbers.
def total_prime(start,end):
    count=0
    for i in range(start,end+1):
        is_prime=True
        for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            count+=1
    return count
start= int(input("Enter a number: "))
end= int(input("Enter a number: "))
result=total_prime(start,end)
print(result)