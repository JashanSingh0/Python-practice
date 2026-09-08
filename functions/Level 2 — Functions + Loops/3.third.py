# Function to count primes up to n.
def count_primes(number):
    count=0
    for i in range(2,number+1):
        is_prime=True
        for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            count+=1
    return count
number= int(input("Enter a number: "))
result=count_primes(number)
print(result)

# Function to return all factors.
def factors(number):
    new_list=[]
    for i in range(1,number+1):
            if number%i==0:
                new_list.append(i)
    return new_list
number= int(input("Enter a number: "))
result=factors(number)
print(result)

# Function to count factors.
def count_factors(number):
    if number==0:
        return 'infinite factors'
    count=0
    for i in range(1,number+1):
            if number%i==0:
                count+=1
    return count
number= int(input("Enter a number: "))
result=count_factors(number)
print(result)

# Function to calculate GCD.
def find_gcd(a,b):
    smaller = a if a<b else b
    if a==0 or b==0:
        return max(a,b)
    gcd=1   
    for i in range(1,smaller+1):
            if a%i==0 and b%i==0:
                gcd=i
    return gcd
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
result=find_gcd(a,b)
print(result)

# Function to calculate LCM.
def find_lcm(a,b):
    larger=a if a>b else b  
    if a == 0 or b == 0:
        return 0
    for i in range(larger,a*b+1):
            if i%a==0 and i%b==0:
                return i
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
result=find_lcm(a,b)
print(result)