import sys
input = sys.stdin.readline

n = int(input())
vote = int(input())
vote_all = [vote] + list(map(int, input().split()))
vote_all.sort(reverse = True)

print(vote_all.index(vote) + 1)