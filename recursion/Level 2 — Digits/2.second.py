# Find the smallest digit recursively.
def smallest_digit(number,smallest=9):
    number=abs(number)
    if number==0:
        return smallest
    digit=number%10
    if smallest>digit:
        smallest=digit
    return smallest_digit(number//10,smallest)
print(smallest_digit(223))
print(smallest_digit(-978))
print()

# Count occurrences of a digit recursively.
def count_digit(number,digit,first=True):
    number=abs(number)
    if number==0:
        return 1 if first and digit == 0 else 0
    current=number%10
    if current==digit:
        return 1+count_digit(number//10,digit,False)
    return count_digit(number//10,digit,False)
print(count_digit(123,3))
print(count_digit(0,1))
print()

# Check palindrome number recursively.
def check_palindrome(number):
    def reverse_number(number,reverse=0):
        if number<0:
            return -reverse_number(-number)
        
        if number==0:
            return reverse
        digit=number%10
        reverse=reverse*10 +digit
        return reverse_number(number//10,reverse)
    return number==reverse_number(number)
print(check_palindrome(323))
print(check_palindrome(-991))
print()

# Check whether all digits are even recursively.
def all_even(number):
    number = abs(number)
    if number==0:
        return True
    if number%2==0:
        return all_even(number//10)
    return False
print(all_even(246))
print()

# Find the first digit recursively.
def first_digit(number):
    number = abs(number)
    if number<10:
        return number
    return first_digit(number//10)
print(first_digit(246))
print(first_digit(91))
print()