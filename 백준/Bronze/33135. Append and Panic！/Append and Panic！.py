import sys
input = sys.stdin.readline

s = input().strip()

original = []
for i in s[::-1]:
    if i not in original:
        original.append(i)
print(len(s) - len(original))