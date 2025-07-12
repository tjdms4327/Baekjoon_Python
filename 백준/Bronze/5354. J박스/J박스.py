import sys
input=sys.stdin.readline

def box(i):
    if i==1: print('#')
    else:
        print('#'*i)
        for _ in range(i-2):
            print('#'+'J'*(i-2)+'#')
        print('#'*i)
    print()
    
t=int(input().strip())
for _ in range(t):
    i=int(input().strip())
    box(i)
    