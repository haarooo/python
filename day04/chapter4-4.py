
# 1. min , max , sum
numbers = [13,124,141,2,41]
print(min(numbers)) # 최솟값
print(max(numbers)) # 최댓값
print(sum(numbers)) # 합계

 # 2. reversed , 이터레이터 반환 
print(reversed(numbers))
print(list(reversed(numbers)))

for i in reversed(numbers):
    print(i) # 역순으로 출력

# 3. enumerate , 인덱스와 자료 순회 가능
print(enumerate(numbers)) 
print(list(enumerate(numbers))) # 타입 변환 후 출력

for index , value in enumerate(numbers) : 
    print(index , value)

# 4. items
example_dict = {'키A': '값A' , '키B' : '값B', '키C' : '값C'}
print(example_dict.items()) # 리스트 형태로 출력
for key , value in example_dict.items():
    print(key , value)

# 5. 리스트내 반복문 사용 , 0부터 20 사이의 짝수 갖는 리스트
# 5-1
array = []
for i in range(0,20,2):
    array.append(i)
print(array)

# 5-2 [계산식 for 반복변후 in 반복할 수 있는 것 if 조건식]
array = [ i for i in range(0,20,2)]
print(array)

array = [ i for i in range(0,20,2)if i != 10]
print(array)

# 6 문자열 여러줄 입력하기

# 6-1 """ 여러줄 입력 """
print("""
        안녕하세요1
        안녕하세요2
      """)

# 6-2 \n
print("안녕하세요1\n""안녕하세요2")
      
# 6-3 () 소괄호 안에서 여러개 문자 연결
print("안녕하세요\n" "안녕하세요2")

# 6-4 .join() 요소 사이네 조합 문자열 연결 
print("\n".join(["안녕하세요1","안녕하세요2"]))

output=[i for i in range(1,101) if "{:b}".format(i , 'b').count('0') == 1 ]
print(output)
for i in output:
    print("{} : {}".format(i,"{:b}".format(i)))
    print("합계:" , sum(output))