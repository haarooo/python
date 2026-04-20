
# 함수
def 함수명 () :
    print('안녕하세요')
    print('안녕하세요')
    print('안녕하세요')


함수명()

# 매개변수 : 함수 호출/사용할 때 인자값 저장하는 변수
def func2(value , n):
    for i in range(n):
        print(value , n)
        
func2("안녕하세요", 5)

# 가변 매개변수 , 매개변수의 개수가 변할 수 있다
def func3(n , *values): # 매개변수에 *가변매개변수 사용시 [리스트]타입 받는다
    for i in range(n):
        for value in values: # values = ["안녕하세요" , "즐거운" ]
            print(value)
        print()

func3(3, "안녕하세요" , "즐거운" , "파이썬")    

# 기본 매개변수 : 만약에 함수 사용/호출할 때 인자값이 없으면 기본값 대입
def func4(value , n = 2): # 매개변수에 변수명 = 기본값으로 인자값이 없을때 대입된다 
    for i in range(n):
        print(value)

func4("안녕하세요") 

# 키워드 매개변수 : 매개변수 이름을 직접 지정하여 매개변수에 대입하는 방법
def func5(*values , n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()    

func5("안녕하세요" , "즐거운" , "파이썬" , 3) # n에 대입 실패
func5("안녕하세요" , "즐거운" , "파이썬" , n=3) # n에 대입

# 리턴 : 함수 종료시 반환되는 키워드

# 반환값 없는 리틴
def func6():
    return
print(func6()) # 반환값이 없다

# 반환값 있는 리턴
def func7():
    return 100
print(func7())

