s=input()
mobis=['M', 'O', 'B', 'I', 'S']

judge="YES"
for i in range(5):
    if mobis[i] not in s:
        judge="NO"
        break
print(judge)