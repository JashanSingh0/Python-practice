# Find the last digit of a number.
num=abs(int(input("Enter a number: ")))
last_digit=num%10
print(last_digit)

# Remove the last digit repeatedly and print each intermediate number.
num=abs(int(input("Enter a number: ")))
if num==0:
    print(0)
else:
    while num>0:
        num= num//10
        print(num)

# Print every digit of a number separately.
num=abs(int(input("Enter a number: ")))
if num==0:
    print(0)
else:
    divisor=1
    while num//divisor>=10:
        divisor*=10
      
    while divisor>0:
        digit=num//divisor
        print(digit)
        num=num%divisor
        divisor=divisor//10


# Find the difference between the largest and smallest digit.
num=abs(int(input("Enter a number: ")))
smallest_digit=9
largest_digit=0
if num==0:
    print(0)
else:
    while num>0:
        current_digit=num%10
        if current_digit<smallest_digit:
            smallest_digit=current_digit
        if current_digit>largest_digit:
            largest_digit=current_digit
        num=num//10
    print(largest_digit-smallest_digit)

# Find the second-largest digit in a number.
num=abs(int(input("Enter a number: ")))
largest_digit=-1
second_largest=-1
while num>0:
    current_digit=num%10
    if current_digit>largest_digit:
        second_largest=largest_digit
        largest_digit=current_digit
    elif current_digit>second_largest and current_digit!=largest_digit:
        second_largest=current_digit
    num=num//10
if second_largest == -1:
    print("No second-largest digit")
else:
    print(second_largest)