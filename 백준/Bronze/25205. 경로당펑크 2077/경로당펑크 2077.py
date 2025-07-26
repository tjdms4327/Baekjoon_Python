import sys
input=sys.stdin.readline

n=int(input())
s=input().strip()

consonants='qwertasdfgzxcv'
print(1 if s[-1] in consonants else 0)