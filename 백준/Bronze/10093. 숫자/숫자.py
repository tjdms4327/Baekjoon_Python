import sys
input=sys.stdin.readline

ns=list(map(int, input().split()))
ns.sort()

ran=ns[-1]-ns[0]-1
if ran<=1:
    ran=0
print(ran)
nums=[str(i) for i in range(ns[0]+1,ns[-1])]
sys.stdout.write(' '.join(nums)+'\n')