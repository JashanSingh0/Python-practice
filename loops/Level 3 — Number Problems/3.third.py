# Find the total of even digits.
num=abs(int(input("Enter a number: ")))
total=0
if num==0:
    total=1
else:
    while num>0:
        current_digit=num%10
        if current_digit%2==0:
            total+=current_digit
        num=num//10
print(total)

# Find the total of odd digits.
num=abs(int(input("Enter a number: ")))
total=0
while num>0:
    current_digit=num%10
    if current_digit%2==1:
        total+=current_digit
    num=num//10
print(total)

# Check whether a number contains digit 0.
num=abs(int(input("Enter a number: ")))
count=0
while num>0:
    current_digit=num%10
    if current_digit==0:
        count+=1
    num=num//10
print(count>0)

num=abs(int(input("Enter a number: ")))
contain_zero=False
while num>0:
    current_digit=num%10
    if current_digit==0:
        contain_zero=True
        break
    num=num//10
print(contain_zero)
    

# Check whether all digits of a number are even.
num=abs(int(input("Enter a number: ")))
all_even=True
while num>0:
    current_digit=num%10
    if current_digit%2==1:
        all_even=False
        break
    num=num//10
print(all_even)

# Find the first digit of a number.
num=abs(int(input("Enter a number: ")))
if num==0:
    first_digit=0
else:
    while num>0:
        first_digit=num%10
        num=num//10
print(first_digit)