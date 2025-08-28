import sys
input = sys.stdin.readline


n = int(input())
for _ in range(n):
    s = input().strip()

    vowels = sum(1 for i in s if i in 'aeiou')
    consonants = len(s) - vowels

    print(s)
    if vowels > consonants:
        print(1)
    else:
        print(0)