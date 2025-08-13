import sys
input=sys.stdin.readline

x,y=map(int, input().split())
d=int(input())



half=(100*x+y)//2 
short=(half - d)//2
long=half-short

print(long//100, long%100)
print(short//100, short%100)
