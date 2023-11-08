def prime_number(n):
    for i in range(2,n):
        if n %i == 0:
            return False
        else:
            return True

def first_prime_number(n):
    for i in range(n):
        prime_number(n)