# 파이썬 조건문  , if 조건 :
number = int(input("정수 입력>"))

if number > 0 :
    print("양수입니다") # java와 다르게 들여쓰기 이용하여 실행문 구분

if number <0 :
    print('음수입니다')

if number == 0:
    print('0입니다')


# if ~ else
number = int(input('정수 입력>'))
if number %2 ==0:
    print('짝수')
else :
    print('홀수')

# if ~ elif ~ elif ~else
if number %2 ==0:
    print('짝수')
elif number %2 ==1:
    print('홀수')
else :
    print('그외')

# 조건이 3개 이상 일때 : 1. if if if 2. if ~ elif
