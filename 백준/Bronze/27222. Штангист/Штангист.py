n=int(input())
training=list(map(int, input().split()))

muscle_gain=0
for i in range(n):
  morning, evening=map(int, input().split())
  diff=evening-morning
  if (training[i]==1) and (diff>0): muscle_gain+=diff
print(muscle_gain)