n = int(input())
A = list(map(int, input().split()))
cnt = 0
t = 1
for i in A:
    if i != t:
        cnt += 1
    else:
        t += 1
print(cnt)