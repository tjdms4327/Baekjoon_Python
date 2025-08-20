scores = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

sa, sb = map(int, input().split())
a, b = [], []
for i in scores:
    if sa >= i:
        sa -= i
        a.append(i)
    if sb >= i:
        sb -= i
        b.append(i)

c = 0
for i in scores:
    if (i in a) and (i not in b):
        c += i
    elif (i not in a) and (i in b):
        c += i
print(c)