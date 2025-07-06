nums=list(map(int, input().split()))

n_desc=sorted(nums)
if nums==n_desc:
    print('Good')
else:
    print('Bad')