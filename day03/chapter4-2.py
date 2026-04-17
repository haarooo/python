
# 딕셔너리란? 키를 기반으로 값을 저장하는 것
# vs JS(json) vs JAVA(map/dto)

# 선언
dict_a = {"name": "어벤져스" , "type" : "영화"}

# 호출
print(dict_a)
print(dict_a["name"])
print(dict_a.get("name")) # java map처럼 호출 가능
# print(dict_a["orgin"]) # 존재하지 않는 키 error

# 딕셔너리 값 추가
dict_a['price'] =1000
print(dict_a)

dict_a['price'] = 2000 # 존재하면 수정 , key는 중복 볼가능
print(dict_a)

# 딕셔너리 키/값 제거
del dict_a['price']
print(dict_a)

# 반복문과 딕셔너리 관계
# for 키 in 딕셔너리명:
#   실행문
for key in dict_a:
    print(key,":",dict_a[key])

pets = [{'name' : '구름' , "age" : 5},
        {'name' : '초코' , "age" : 3},
        {'name' : '아지' , "age" : 1},
        {'name' : '호랑이' , "age" : 1}
        ]
print(pets)
for key in pets:
    print( key['name'] , key['age'],'살')

numbers = [1,5,2,4,5,1,6,3,5,1,4,2,4,]
counter = {}
for number in numbers:
    if number in counter:
        counter[number]+= 1
    else :
        counter[number] = 1
       

character = {"items" : {"name": "기사"}}

for key in character:
    if type(character[key]) is dict :
        for element in character[key]:
            print(element , ':' , character[key][element])
    elif type(character[key]) is list :
        for element in character[key]:
            print(key,":" , element)
    else:
        print(key , ':' , character[key])
            