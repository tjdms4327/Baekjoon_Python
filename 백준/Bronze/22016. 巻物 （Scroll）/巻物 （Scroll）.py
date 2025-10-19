n, k = map(int, input().split())
s = input().strip()

print(s[:k-1] + s[k-1:].swapcase())