# Write a function that calls another function.
def hello():
    print("Hello")

def start():
    hello()
start()

def add(a,b):
    return a+b
def calc_print(a,b):
    result=add(a,b)
    print(result)
calc_print(3,7)


# Write a function that accepts another function as an argument.
def run_function(function):
    print(function(15,5)) 
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a/b
run_function(add)
run_function(subtract)
run_function(multiply)

# Write a function that returns another function.
def add(a,b):
    return a+b
def calc_print():
    return add
operation= calc_print()                 # operation now pointing to add func
print(operation(3,4))

# Write a function that calculates n! and use it inside another function.
def factorial(number):
    result=1
    if number<0:
        return -1
    for i in range(1,number+1):
        result*= i
    return result
def multiply():
    return 2*factorial(5)
print(multiply())

# Write a function that checks whether a number is prime and use it to print primes.
def check_prime(number):
    if number<2:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True
def print_primes(number):
    result= check_prime(number)
    if result:
        print(number)
print_primes(19)