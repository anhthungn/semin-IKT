from linear_search import linear_search
from binary_search import binary_search
import time
import random

array = list(range(1, 1000000))
target = random.randint(0, 9999999)

start = time.time()
linear_result = linear_search(array, target)
end = time.time()

print(end - start)

start = time.time()
binary_result = binary_search(array, target)
end = time.time()

print(end - start)