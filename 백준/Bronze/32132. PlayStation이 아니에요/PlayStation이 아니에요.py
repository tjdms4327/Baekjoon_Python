import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

while "PS4" in s or "PS5" in s:
    s = s.replace("PS4", "PS")
    s = s.replace("PS5", "PS")
print(s)
