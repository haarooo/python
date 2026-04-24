
# OS모듈

import os # OS모듈
print(os.name) # nt : 윈도우
print(os.getcwd()) # 현재 최상위 폴더
print(os.listdir()) # 현재 최상위 폴더의 내부 요소

os.mkdir('hello') # 폴더 생성
os.rmdir('hello') # 폴더 삭제

with open('original.txt' , 'w') as file:
    file.write("hello")

os.rename('./day08/original.txt' , './day08/new.txt') # 파일명 변경

os.remove('./day08/new.txt') # 파일 삭제

os.system('dir') # 시스템 명령어 실행 

# datetime 모듈

import datetime

print(datetime.datetime.now()) # 현재시간
now = datetime.datetime.now()
print(now.year)
print(now.day)
print(now.month)
print(now.hour)
print(now.minute)
print(now.second)
# 형식 : Y년 m월 d일 H시 M분 S초
now.strftime('%Y-%m-%d / %H:%M:%S')

#시간 계산
output = now.replace(year=(now.year+1) , month = (now.month -1))
print(output)


# time 모듈
import time
print('3초간 일시정지')
time.sleep(3)

# urllib모듈
from urllib import request # from 이용하여 특정한 함수/변수만 가져오기

target = request.urlopen('https://google.com')
output = target.read()

print(output)

import os 
output = os.listdir(".")
print("os.listdir():" , output)
print()

print("# 폴더와 파일 구분하기")
for path in output :
    if os.path.isdir(path):
        print("폴더:",path)
    else:
        print("파일",path)


