
# 변수 : 하나의 자료 저장하는 공간
pi = 123.123 #변수 선언
print(pi) # 변수 참조


# print(pi +"입니다") 숫자 자료형이기 때문에 타입 오류 발생
print(pi , "입니다") #  , = 연결


# 복합 대입 연산자
number = 100
number += 10
number *= 10
number /= 10
number %= 10
number //= 10
number **= 2
print(number)

string = '안녕하세요'
string *= 3
print(string)

# 사용자 입력 , input()
input("인사말을 입력하세요>") # 콘솔에 입력하는 구조로 무조건 문자열로 반환된다

string = input('인사말을 입력하세요>')
print(string)
print(type(string))

# 문자열을 숫자로 변환하기 , 사용처 : input , HTTP(API , JSON 등) , 자바 = Intger.parseint()vs 자바스크립터 = parseint() vs 파이썬 = int()
int_a = int(string)
print(type(int_a))

string_b = int(input("입력b >"))
print(string_b)

string_c = float(input("입력c > "))
print(type(string_c))

# 숫자를 문자열로 바꾸기

pi = 3.14
string_d= str(pi)
print(type(string_d))