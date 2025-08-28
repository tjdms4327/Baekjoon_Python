import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

max_len = max(len(a), len(b))
a = a.zfill(max_len)
b = b.zfill(max_len)


res = []
for d1, d2 in zip(a, b):
    d1, d2 = int(d1), int(d2)
    if (d1 <= 2 and d2 <= 2) or (d1 >= 7 and d2 >= 7):
        res.append('0')
    else:
        res.append('9')
print(''.join(res))