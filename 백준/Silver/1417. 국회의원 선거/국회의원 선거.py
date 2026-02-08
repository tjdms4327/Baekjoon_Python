import sys
input = sys.stdin.readline

n = int(input())
votes = [int(input()) for _ in range(n)]

count = 0
while votes[0] != max(votes):
    idx = votes.index(max(votes))
    count += 1
    votes[0] += 1
    votes[idx] -= 1
if votes.count(max(votes))>1:
    count += 1
    
print(count)