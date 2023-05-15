def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5 ) + 1):
        if number % i == 0:
            return False
    return True
def prime_number(n):
    print("prime numbers form 0 to " , n, ":")
    for number in range(n + 1 ):
        if is_prime(number):
            if is_prime(number):
                print(number)

n=20
prime_number(n)