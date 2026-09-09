# # Find nth Fibonacci number recursively.
# def nth_fibonacci(number,a=0,b=1):
#     if number==1:
#         return a    
#     return nth_fibonacci(number-1,b,a+b)
# print(nth_fibonacci(5))

# # Print first n Fibonacci numbers recursively.
# def n_fibonacci(number,a=0,b=1):
#     if number==0:
#         return   
#     print(a)    
#     n_fibonacci(number-1,b,a+b)
# n_fibonacci(5)

# Check whether a number is Fibonacci recursively.
def check_fibonacci(number,a=0,b=1):
    if a>number:
        return False
    if a==number:
        return True        
    return check_fibonacci(number,b,a+b)
print(check_fibonacci(6))


# Calculate GCD recursively.
def find_gcd(a,b):                      #Euclidean algorithm
    if b==0:
        return a
    return find_gcd(b,a%b)
print(find_gcd(6,4))

# Calculate LCM using recursive GCD.
def find_lcm(a,b):                       
    gcd=find_gcd(a,b)
    lcm=(a//gcd)*b                       #or lcm = (a*b)//gcd
    return lcm
print(find_lcm(6,4))
