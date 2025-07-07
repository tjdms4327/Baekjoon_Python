import sys
input=sys.stdin.readline

n,a,b=map(int, input().split())
positive, negative=1,1
for _ in range(n):
    positive, negative=positive+a, negative+b
    if positive<negative:
        positive, negative=negative, positive
    elif positive==negative:
        negative-=1
print(positive,negative)