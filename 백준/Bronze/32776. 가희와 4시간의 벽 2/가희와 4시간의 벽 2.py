rail=int(input())
ma,f,mb=map(int, input().split())
flight=ma+f+mb

if rail<=flight or rail<=240:
    print('high speed rail')
elif rail>flight:
    print('flight')