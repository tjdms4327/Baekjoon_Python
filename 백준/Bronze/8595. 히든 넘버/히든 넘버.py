# bronzeI_8595
import sys, re
input = sys.stdin.readline

n = int(input())
s = input().strip()

nums = re.findall(r'\d+', s)
print(sum(map(int, nums)))