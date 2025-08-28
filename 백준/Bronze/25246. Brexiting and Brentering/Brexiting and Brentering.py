import sys
input = sys.stdin.readline

s = input().strip()

vowels = "aeiouAEIOU"
idx = max(s.rfind(v) for v in vowels)
print(s[:idx+1] + 'ntry')