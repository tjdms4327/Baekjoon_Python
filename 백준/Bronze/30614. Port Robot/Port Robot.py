import sys
input=sys.stdin.readline


n=int(input())
s=input().strip()

container=[]
for char in s:
    if char.islower():
        container.append(char)
    elif container and (char.lower() == container[-1]):
        container.pop()
    else:
        print(0)
        break
else:
    if not container:
        print(1)
    else:
        print(0)