import sys
input=sys.stdin.readline

first=int(input().strip())
second=int(input().strip())
third=int(input().strip())
if (first in [1, 3]) and (second in [6, 8]) and (third in [2, 5]):
    print("JAH")
else: print("EI")