n=int(input())

small, big=2, n-1
while n%small==0:
    small+=1
while n%big==0:
    big-=1
print(small, big)