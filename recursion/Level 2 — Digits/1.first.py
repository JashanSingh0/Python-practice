# Count digits recursively.
def count_digits(number,first=True):
    number=abs(number)
    if number==0:
        return 1 if first else 0
    return 1+count_digits(number//10,False)
print(count_digits(123))
print(count_digits(0))
print()

# Find digit sum recursively.
def sum_digits(number):
    number=abs(number)
    if number==0:
        return 0
    return number%10+sum_digits(number//10)
print(sum_digits(123))
print(sum_digits(-991))
print()

# Find product of digits recursively.
def product_digits(number):
    number=abs(number)
    if number==0:
        return 1
    return number%10*product_digits(number//10)
print(product_digits(123))
print(product_digits(-991))
print()

# Reverse a number recursively.
def reverse_num(number,reverse=0):
    if number<0:
        return -reverse_num(-number)
    
    if number==0:
        return reverse
    digit=number%10
    reverse=reverse*10 +digit
    return reverse_num(number//10,reverse)
print(reverse_num(123))
print(reverse_num(-991))
print()

# Find the largest digit recursively.
def largest_digit(number,largest=0):
    number=abs(number)
    if number==0:
        return largest
    digit=number%10
    if largest<digit:
        largest=digit
    return largest_digit(number//10,largest)
print(largest_digit(123))
print(largest_digit(-991))
print()