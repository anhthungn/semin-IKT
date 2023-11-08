def eratosthenes_sieve(n):
    numbers = [True]*(n + 1)
    numbers[0] = False
    numbers[1] = False
    prvocislo = []
    
    for i in range(n):
        if numbers[i]:
            prvocislo.append(i)

            for x in range(i*2, n, i):
                numbers[x] = False
    
    return prvocislo





