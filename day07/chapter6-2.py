
# 예외객체 : Exception 클래스
# except 예외클래스명 as 변수명
# 모든 예외 잡기 : 마지막에 Exception클래스 사용
# 강제 예외 발생 : 1. 미구현 , 2.웹/앱 프레임워크(유효성검사/트랜잭션)

list_number = [12,424,53,31,53]

try:
    number_input = int(input('정수입력 >'))
except ValueError as e:
    print('정수만 입력하세요')
except IndexError as e:
    print('인덱스 벗어남')
except Exception as e:
    print(e)



