# 문자열의 format()함수
string_a = "{}".format(10)
print(string_a , type(string_a))

format_a = "{}만 원".format(5000)
print(format_a)
format_b = "{}{}{}".format(1, "유재석" , True)
print(format_b)

# 특정 칸에 출력하기
output_a = "{:5d}".format(52)
print(output_a)
output_b = "{:05d}".format(52)
print(output_b)

# 기호를 붙여 출력하기
output_c = "{:+d}".format(52)
print(output_c)
output_d = "{:+d}".format(-52)
print(output_d)

# 부동 소수좀 출력하기
output_e = "{:015f}".format(52.273)
print(output_e)
output_f = "{:+015f}".format(25.252)
print(output_f)
output_g = "{:15.3f}".format(25.2525)
print(output_g)

# 의미 없는 소수점 제거하기
output_g ="{:g}".format(52.0)
print(output_g,type(output_g))

# 대소문자 바꾸기
a = "Hello Python"
print(a.upper()) # 대문자로 변경
print(a.lower())

# 공백 제거하기
b =         "안녕하세요"
print(b.strip()) # 양쪽 공백제거 , lstrip(왼) , rstrip(오)

# 문자열 찾기
out_a = "안녕안녕하세요".find("안녕")
print(out_a)
out_b = "안녕안녕하세요".rfind("안녕")
print(out_b)

# in연산자
print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")

# 문자열 자르기
out_c = "10 20 30 40 50".split(" ")
print(out_c)

# f-문자열 vs .format()
print(f'{10}')
print("{}".format(10))


r = 5
rs = (5**3)*4/3*3.141592

a = 3.0
b = 4.0
c = (4.0**2 + 3.0**2)**(1/2)
print(c)
