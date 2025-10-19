n = int(input())
s = input().strip()

count = 0
for i in range(n):
    if i%2 == 0 and s[i] != 'I':
        count += 1
    elif i%2==1 and s[i] != 'O':
        count += 1
print(count)