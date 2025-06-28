from itertools import combinations
def subset(list):
  cand=[]
  for subset in combinations(list, 3):
    digit_one=sum(subset)%10 ; cand.append(digit_one)
  return max(cand)

n=int(input())
winner, winner_digit=0, 0
for i in range(1,n+1):
  cards=list(map(int, input().split()))
  if subset(cards)>=winner_digit:
    winner, winner_digit=i, subset(cards)
print(winner)