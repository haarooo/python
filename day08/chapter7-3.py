
# 모듈 만들기 : .py파일 만들기와 같다
# 1. xxx.py 파일 생성 
# 2. 다른 파일에서 import하여 호출

import test_module as test

radius = test.number_input()
print(test.get_circum(radius))
print(test.get_circle_area(radius))

# 프로그램의 진입점 : __name__ == "__main__"
print(__name__)


# 인터넷의 이미지 저장하기

from urllib import request

target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

file = open("output.png","wb")
file.write(output)
file.close()