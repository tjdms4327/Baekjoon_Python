n = int(input())
s = input().strip()

word = 'BRONZESILVER'
count = [0]*10  # B, R, O, N, Z, E, S, I, L, V
for ch in s:
    for i in range(10):
        if ch == word[i]:
            if ch in 'ER':
                count[i] += 0.5
            else:
                count[i] += 1

result = int(min(count))
print(result)
