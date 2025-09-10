checkList = [0] * 4 # 비밀번호 체크 리스트
myList = [0] * 4 # 현재 상태
checkSecret = 0 # 몇 개의 문자가 개수 조건 충족했는지

def myadd(c): # 새로 들어온 문자 처리
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c): # 제거되는 문자 처리
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

        
s, p = map(int, input().split()) # DNA 문자열 길이, 비밀번호 길이
DNA = list(input().strip())
checkList = list(map(int, input().split()))
result = 0

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(p): # 초기 p부분 문자열 처리
    myadd(DNA[i])
if checkSecret == 4:
    result += 1

for i in range(p, s):
    j = i - p
    myadd(DNA[i])
    myremove(DNA[j])
    if checkSecret == 4:
        result += 1
print(result)