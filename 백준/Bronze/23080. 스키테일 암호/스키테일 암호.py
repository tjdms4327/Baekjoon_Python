n=int(input())
s=input()
print(*[s[i] for i in range(0, len(s), n)], sep='')