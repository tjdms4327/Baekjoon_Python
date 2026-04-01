import sys
input=sys.stdin.readline

while True:
    num=input().strip()
    if num=='0': break

    while int(num)>=10:
        digits=list(map(int, num))
        num=str(sum(digits))
    print(num)