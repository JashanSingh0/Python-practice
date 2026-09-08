# Find the largest digit in a number.
num=abs(int(input("Enter a number: ")))
largest_digit=0
while num>0:
    current_digit=num%10
    if current_digit>largest_digit:
        largest_digit=current_digit
    num=num//10
print(largest_digit)

# Find the smallest digit in a number.
num = abs(int(input("Enter a number: ")))
smallest_digit = 9
while num>0:
    current_digit= num%10
    if smallest_digit>current_digit:
        smallest_digit=current_digit
    num= num//10
print(smallest_digit)

# Count how many times digit 5 occurs in a number.
count=0
num = abs(int(input("Enter a number: ")))
while num>0:
    current_digit= num%10
    if current_digit==5:
        count+=1
    num=num//10
print(count)

# Count the number of even digits.
count=0
num = abs(int(input("Enter a number: ")))
while num>0:
    current_digit= num%10
    if current_digit%2==0:
        count+=1
    num=num//10
print(count)

# Count the number of odd digits.
count=0
num = abs(int(input("Enter a number: ")))
while num>0:
    current_digit= num%10
    if current_digit%2==1:
        count+=1
    num=num//10
print(count)
