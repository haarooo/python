
# 에외처리 : 예외가 발생할 상활을 예측하고 모두 조건문으로 처리하는 것이 힘들다
# 에외가 발생하면 프로그램이 강제로 종료되지 않게 흐름 제어하기 = 예외처리
# try: ~ except:

try:
    int(input('정수입력 : '))
except: 
    print('정수만 입력하세요')


list_input = ["52","252","32","스파이","103"]
list_number = []
for item in list_input:
    try:
        float(item)
        list_number.append(item)
    except:
        pass # 예외 발생 시 아무 것도 하지 않고 일단 통과

# else : 예외가 발생하지 않았을 때 실행 코드

try:
    number_input = int(input('정수 입력 :'))
except:
    print('정수를 입력하세요')
else: 
    print(number_input)


# finally : 무조건 실행할 코드

try:
    number_input = int(input('정수 입력 :'))
except:
    print('정수만 입력하세요')
else:
    print(number_input)
finally:
    print('무조건 실행')

[1,2,3,4][10]