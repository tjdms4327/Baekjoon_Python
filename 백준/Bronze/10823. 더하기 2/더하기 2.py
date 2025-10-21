# bronzeI_10823
import sys

s = sys.stdin.read().replace('\n', '')

nums = list(map(int, s.split(',')))
print(sum(nums))