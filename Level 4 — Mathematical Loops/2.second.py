# Find all factors of a number.
num=abs(int(input("Enter a number: ")))
if num==0:
    print("Infinite factors")
else:
    for i in range(1,num+1):
        if num%i==0:
            print(i)

# Count the factors of a number.
num=abs(int(input("Enter a number: ")))
count=0
if num==0:
    print("Infinite factors")
else:
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    print(count)

# Find the sum of all factors of a number.
num=abs(int(input("Enter a number: ")))
total=0
if num==0:
    print("Infinite")
else:
    for i in range(1,num+1):
        if num%i==0:
            total+=i
    print(total)

# Check whether a number is a perfect number.
num=abs(int(input("Enter a number: ")))
total=0
if num==0:
    print(False)
else:
    for i in range(1,num):
        if num%i==0:
            total+=i
print(num==total)

# Print all perfect numbers between 1 and n.
n=abs(int(input("Enter a number: ")))
for i in range(1,n+1):
    total=0
    for div in range(1,i):
        if i%div==0:
            total+=div
    if total==i:
        print(i)