def prime_number(n):
    for i in range(2,n):
        if n %i == 0:
            return False
        else:
            return True

n = int(input("Zadejte číslo "))

if prime_number(n):
    print(n, "je prvočíslo.")
else:
    print(n, "není prvočíslo.")