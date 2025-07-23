from itertools import groupby

for _ in range(3):
    s=input()
    result = [len(list(n)) for i, n in groupby(s)]
    print(max(result))