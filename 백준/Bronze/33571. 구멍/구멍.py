from collections import Counter

one_hole="AabDdegOoPpQqR@"
counter_one = Counter(one_hole)
two_holes='B'

S=input()
holes=sum(counter_one[i] for i in S)+(S.count(two_holes))*2
print(holes)