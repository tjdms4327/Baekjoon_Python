import sys
input=sys.stdin.readline

n, a, b=map(int, input().strip().split())
s, t=map(int, input().strip().split())
if a<s<b and a<t<b: print("City") # 양방향 고려
elif (s<=a and t<=a) or (b<=s and b<=t): # 무조건 s>=1, t<=n이므로 따로 처리할 필요X
    print("Outside")
else: print("Full")