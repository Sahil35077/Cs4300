# Function to check if a number is positive, negative, or zero
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# Function to return the first 10 prime numbers
def prime_numbers():
    primes = []
    num = 2
    while len(primes) < 10:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

# Function to find sum of numbers from 1 to 100
def sum_numbers():
    return sum(range(1, 101))