import sys
input=sys.stdin.readline

n=int(input())
s=input()

trans=str.maketrans("JOI", "OIJ")
result=s.translate(trans)
print(result)