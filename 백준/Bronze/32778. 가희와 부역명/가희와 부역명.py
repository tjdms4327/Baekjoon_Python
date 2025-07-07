import sys
input=sys.stdin.readline

subway=input().strip().split('(')
if len(subway)==1:
    print(*subway, '-', sep='\n')
else:
    print(subway[0], subway[1][:-1] , sep='\n')