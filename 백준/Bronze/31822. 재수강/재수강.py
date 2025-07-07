retake=input()
retake=retake[:5]

N=int(input())
possible=0
for _ in range(N):
    subject=input()
    if retake==subject[:5]:
        possible+=1
print(possible)