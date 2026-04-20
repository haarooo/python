
# 재귀함수란 현재 실행 중인 (자신의)힘수를 다시 호출 하는것

# 1. 반복문으로 팩토리얼 구하기

def factorial(n):
    output =1
    for i in range(1 , n+1):
        output *=i
    return output

factorial(5)

# 2. 재귀함수로 팩토리얼 구하기
def func2(n):
    if n == 0:
        return 1
    else:
        return n*func2(n-1) # 재귀함수 호출
    
print(func2(5))

# 피보나치 수열 
def func3(n):
    if n ==1:
        return 1
    if n ==2:
        return 2
    else:
        return func3(n-1) + func3(n-2)
    
print(func3(5))

# 피보나치 수열 , 메모화
dict = { # 결과를 저장하는 딕셔너리
    1: 1,
    2: 2
}
counter = 0

def func4(n):
    global counter
    counter += 1
    print(counter)
    if n in dict:
        return dict[n]
    else:
        output = func4(n-1)+func4(n-2)
        dict[n] = output
        return output
    
print(func4(6))

min_peo = 2
max_peo = 10
total_peo = 100
memo={}

def func5(n , min_peo): 
    key = str([ n , min_peo])
    if key in memo:
        return memo[key]
    if n<0:
        return 0
    if n==0:
        return 1
    else:
        count = 0
        for i in range(min_peo , max_peo +1):
            count+=func5(n-i , i) # 남은 사람수에 i만큼 제외하고 , i대입
        memo[key] = count
        return count    
    
print(func5(100 , 2))    




