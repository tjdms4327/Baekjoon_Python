digits_12 = "0123456789ab"
digits_16 = "0123456789abcdef"

for n in range(1000, 10000):
    sum_10 = sum(map(int, str(n)))
    sum_16 = sum(digits_16.index(ch) for ch in hex(n)[2:])
    if sum_10 != sum_16:
        continue

    tmp = n
    sum_12 = 0
    while tmp > 0:
        sum_12 += tmp % 12
        tmp //= 12

    if sum_10 == sum_12:
        print(n)