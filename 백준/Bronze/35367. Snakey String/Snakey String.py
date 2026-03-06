n, m = map(int, input().split())

s = [list(input().strip()) for _ in range(n)]

result = ''
for col in zip(*s):
    for x in col:
        if x != '.':
            result += x
            break
print(result)