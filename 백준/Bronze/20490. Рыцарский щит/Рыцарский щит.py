import sys
input=sys.stdin.readline

shield1=list(map(int, input().split()))
shield2=list(map(int, input().split()))
shield1.sort() ; shield2.sort()



touched=sorted([shield1[2], shield2[2]])
distance=sum(shield1[:2])+sum(shield2[:2])+(touched[1]-touched[0])
print(distance)