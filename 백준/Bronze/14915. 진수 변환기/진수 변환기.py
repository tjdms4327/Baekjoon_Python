# bronzeII_14915
import sys
input = sys.stdin.readline

mapping = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

m, n = map(int, input().split())

if m == 0:
    print('0')
else:
    result = []
    while m > 0:
        val = m % n
        result.append(str(mapping.get(val, val)))
        m //= n

    print(''.join(result[::-1]))