import sys
input=sys.stdin.readline

n=int(input())
nums=input().split()

longest=max(map(lambda x: len(x), nums))
nums.sort(key=lambda x: int(x.ljust(longest, '0')), reverse=True)
result=''
for i in nums:
    result=max(i+result, result+i)
if int(result)==0:
    print(0)
else:
    print(result)
