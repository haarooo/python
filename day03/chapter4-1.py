
# 리스트란? 여러 자료들을 모아 하나의 자료로 구성
# [ 1,2,3]
# 인덱스란? 자료 저장된 순서 , 0번 시작 

list_a = [224,32, "문자열" ,True]
print(list_a[0])
print(list_a[1:3])

# 요소값 변경
list_a[1] = "변경값"
print(list_a)

print(list_a[-1])
print(list_a[-2])


print(list_a[2][1])  

list_a[1] = ['변경값1' , '변경값2']
print(list_a)


# 리스트 연산
list_a = [1,2,3]
list_b = [4,5,6]

# 1. 연결
print(list_a+list_b)
# 2. 반복
print(list_a*3)
# 3. 길이
print(len(list_a)) 


# 리스트에 요소 추가 
# 1. 요소 추가하기
list_a.append(4)
print(list_a)
# 2. 중간에 요소 추가
list_a.insert(1,3)
print(list_a)

# 리스트에 요소 제거
list_a =[0,1,2,3,4,5]
# del
del list_a[1]
print(list_a)
# pop
list_a.pop(2)
print(list_a)
list_a.pop()
print(list_a)

# 슬라이싱이란? 인덱스로 구성된 자료들(문자열/리스트)의 요소 선택 기능
# [시작인덱스 : 끝인덱스 : 단계]
print(list_a[::-1]) # 역순으로 출력
print(list_a[0::2]) # 0부터 마지막 인덱스까지 2칸씩 이동

# 리스트명.remove(자료)
list_a.remove(4) # 해당 자료가 존재하면 삭제
print(list_a)


# 리스트명.clear()
list_a.clear()
print(list_a)

# .sorrt() 리스트 정렬 , .sort(reverse=True)
list_a = [12, 425, 16,32]
list_a.sort()
print(list_a)

list_a.sort(reverse=True)
print(list_a)

# in 내부에 있는지 확인
print(103 in list_a)
print(32 in list_a)

# 리스트와 반복문 , 
# for 반복변수 in 반복할자료 :
#  코드

array = [123, 32, 424 , 12, 52]
for element in array:
    print(element)


for element in "안녕하세요":
    print(element)



# 중첩 리스트 , 중첩 반복문 , 2차원 리스트
list_of_list = [
    [1,2,3],     # 1행
    [4,5,6,7],   # 2행
    [8,9]       # 3행
    ]

for row in list_of_list :
    print(row)
    for col in row : 
        print(col)


# 전개 연산자
list_a = [1,3,2]
print(list_a)
print(*list_a) # 리스트는 첫번째 인덱스를 참조한다

print([list_a , list_b]) # 2차원 배열 구성
print([*list_a , *list_a]) #1 차원 배열

numbers =[1,2,3,4,5,6,7,8,9]
output = [[],[],[]]
for number in numbers:
    output[(number-1)%3].append(number)

print(output)    

    
for i in numbers:
    print(i , "는" , len(str(i)) , "자릿수입니다")
    
