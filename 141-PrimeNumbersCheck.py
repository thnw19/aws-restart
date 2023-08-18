# import math module
import math

# set number to check prime number
#target = 250
keyIn = input("Input your number to want to check prime number ")

# create empty list for hold prime number
primes = []


# function to check if prime or not
def primeCheck(n):
    if n <= 1:
        return False
    for i in range(2, (int)(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


#for i in range(2, (target+1)):
for x in range(2, (int)(keyIn)+1):
    if primeCheck(x):
        primes.append(x)
print(primes)