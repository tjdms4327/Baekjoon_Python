import sys
input = sys.stdin.readline

s = input().strip()

vowels = set("aeiou")
pattern1 = all((ch in vowels) == (i % 2 == 0) for i, ch in enumerate(s))
pattern2 = all((ch in vowels) == (i % 2 == 1) for i, ch in enumerate(s))

print(1 if pattern1 or pattern2 else 0)