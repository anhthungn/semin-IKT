def nejvetsi_delitel(x, y):
    mensi_cislo = min(x, y)
    nsd = 1
    for i in range(1, mensi_cislo + 1):
        if x%i == 0 and y%i == 0:
            nsd = i
    print(nsd)

nejvetsi_delitel(24, 60)