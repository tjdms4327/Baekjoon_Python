import sys
input=sys.stdin.readline

n=int(input())
ingredients=set(input().strip().split())
used=set(input().strip().split()) 


print(*(ingredients-used))