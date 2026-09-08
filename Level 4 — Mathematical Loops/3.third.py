# Find the GCD of two numbers using a loop.
a=abs(int(input("Enter a number: ")))
b=abs(int(input("Enter a number: ")))
gcd=1
smaller=min(a,b)
for i in range(1,smaller+1):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)

# Find the LCM of two numbers.
a=abs(int(input("Enter a number: ")))
b=abs(int(input("Enter a number: ")))
lcm=0
if a == 0 or b == 0:
    print(0)
else:
    larger = max(a,b)
    for num in range(larger,a*b):
        if num%a==0 and num%b==0:
            lcm=num
            break
    else:
        lcm=a*b
    print(lcm)

# Check whether two numbers are coprime.
a=abs(int(input("Enter a: ")))
b=abs(int(input("Enter b: ")))
gcd=1
if a>b:
    n=b
else:
    n=a
for i in range(1,n+1):
    if a%i==0 and b%i==0:
        gcd=i
if gcd==1:
    print("Coprime")
else:
    print("Not coprime")

# Print the multiplication table of a number.
n=abs(int(input("Enter a number: ")))
for i in range(1,11):
    print(f'{n} × {i} = {n*i}')
    
# Print multiplication tables from 1 to 10.
for n in range(1,11):
    for i in range(1,11):
        print(f'{n} × {i} = {n*i}')
    print("")