# [ Python practice3 ]
# [ 제출방법 ] 코드가 작성된 파일이 위치한 깃허브 상세 주소를 제출하시오.

# 문제 1: 인덱싱과 슬라이싱 리스트 list_data = [10, 20, 30, [40, 50, 60], 70]가 있습니다. 슬라이싱과 인덱싱을 사용하여 다음 결과가 나오도록 코드를 작성하시오.
# 출력 결과 1: [20, 30] (슬라이싱 이용)
# 출력 결과 2: 60 (중첩 리스트 인덱싱 이용)

list_data = [10, 20, 30, [40, 50, 60], 70]
print(list_data[1:3])
print(list_data[3][2])




# 문제 2: 리스트 요소 변경 및 역순 출력 리스트 colors = ["red", "green", "blue"]가 있습니다. "green"을 "yellow"로 변경하고,  리스트의 요소를 역순(['blue', 'yellow', 'red'])으로 출력하시오.
colors = ["red", "green", "blue"]
colors[1] = "yellow"
print(list(reversed(colors)))


# 문제 3: 요소 추가 및 삽입 빈 리스트 my_list = []를 생성한 후, .append()를 사용하여 숫자 10, 30을 순서대로 추가하고, .insert()를 사용하여 10과 30 사이에 숫자 20을 삽입하여 [10, 20, 30]을 만드시오.

my_list = []
my_list.append(10)
my_list.append(30)
my_list.insert(1, 20)
print(my_list)


# 문제 4: 요소 제거 실습 리스트 nums = [0, 1, 2, 3, 4, 5]에서 다음 지시대로 요소를 제거하고 최종 리스트를 출력하시오.
# del을 사용하여 인덱스 0번 요소 삭제
# .pop()을 사용하여 마지막 요소 삭제
# .remove()를 사용하여 값 3 삭제

nums = [0, 1, 2, 3, 4, 5]
del nums[0]
nums.pop()
nums.remove(3)
print(nums)



# 문제 5: 리스트 정렬과 포함 여부 score = [85, 95, 70, 100] 리스트를 내림차순(큰 숫자부터)으로 정렬하고, 사용자로부터 숫자를 입력받아 해당 숫자가 score 리스트 안에 있는지 in 연산자를 사용하여 True/False로 출력하시오.

score = [85, 95, 70, 100]
score.sort(reverse=True)
num1 = int(input('숫자 입력>'))
num1 in score


# 문제 6: 딕셔너리 기본 선언 및 호출 다음 정보를 담은 딕셔너리 movie를 선언하고, .get() 메서드를 사용하여 영화의 "감독"을 출력하시오.
# 제목: 파묘
# 감독: 장재현
# 개봉: 2024

movie = {"제목" : "파묘" , "감독" : "장재현" , "개봉" : 2024}
print(movie.get("감독"))
