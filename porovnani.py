from prime_numbers import eratosthenes_sieve
from prvocislo import first_prime_number
import time

start = time.time()
first_prime_number(100000)
end = time.time()

print(end - start)