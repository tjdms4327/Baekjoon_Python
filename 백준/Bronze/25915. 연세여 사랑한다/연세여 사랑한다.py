import sys
input=sys.stdin.readline

# 'ILOVEYONSEI' 이동은 3+3+7+17+20+10+1+5
movement=84
c=ord(input().strip()) 
# movement에 (c 아스키코드값 - 'I'의 아스키코드값)의 절댓값 더하면됨
print(movement+abs(c-ord('I')))