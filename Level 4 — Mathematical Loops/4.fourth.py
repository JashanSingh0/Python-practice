# Generate the first n Fibonacci numbers.
n=int(input("Enter a number: "))
a,b=0,1
for i in range(n):
    print(a)
    a,b=b,a+b

# Find the nth Fibonacci number using a loop.
n=int(input("Enter a number: "))
a,b=0,1
if n==1:
    print(a)
else:
    for i in range(2,n):
        a,b=b,a+b
    print(b)

# Check whether a number belongs to the Fibonacci sequence.
n=int(input("Enter a number: "))
a,b=0,1
is_fibonacci=False
while a<=n:
    if n==a:
        is_fibonacci=True
        break
    a,b=b,a+b
print(is_fibonacci)

# Check whether a number is an Armstrong number.
n = int(input("Enter a number: "))
original = n
temp = n

digits = 0
while temp > 0:
    digits += 1
    temp //= 10

temp = original
result = 0

while temp > 0:
    digit = temp % 10
    result += digit ** digits
    temp //= 10

print(result == original)


# Print Armstrong numbers between 1 and n.
n=int(input("Enter a number: "))
for i in range(1,n+1):
    original=i
    temp=i
    count=0
    while temp>0:
        count+=1
        temp//=10
    temp=original
    result=0
    while temp>0:
        digit=temp%10
        result+=digit**count
        temp//=10
    if result==original:
        print(original)

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    original = i
    temp = i

    digits = 0
    while temp > 0:
        digits += 1
        temp //= 10

    temp = original
    result = 0

    while temp > 0:
        digit = temp % 10
        result += digit ** digits
        temp //= 10

    if result == original:
        print(original)

