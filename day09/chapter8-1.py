
# 객체 : 속성(상태)거ㅣ 메소드(행동)로 이루어진 추상화
# 클래스 : 객체를 프로그래밍에서 표현하기 위한 설계도
# 인스턴스 : 클래스 기반으로 생성한 객체
# 생성자 : 인스턴스가 생성될 때 실행되는 함수 = 초기화 함수 역할

# 1. 클래스 만들기
class Student :
    # 생성자
    def __init__(self,name , korean , math , english , science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    # 메소드 = 멤버함수 = 인스턴스함수 = 함수
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    def get_average(self):
        return self.get_sum() / 4
    def __eq__(self , value):
        return self.get_average() == value

    def to_string(self):
        return "{}\t{}\t{}".format(self.name , self.get_sum() , self.get_average())

# 인스턴스 생성하기
students = [
    Student("윤인성" , 87,98,88,95),
    Student("연하진" , 87,98,88,95),
    Student("구지연" , 87,98,88,95),
    Student("나선주" , 87,98,88,95),
    Student("윤아린" , 87,98,88,95),
    Student("윤명월" , 87,98,88,95)
]

# 인스턴스내 속성값 호출
print(students[0].name)
# 인스턴스내 메소드 호출
print(students[0].to_string())
# 클래스는 어떠한 구조를 미리 설계하여 통일 되고 상태와 행동 오차 줄일 수 있다



class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    
class StudentList:
    def __init__(self):
        self.students = []
    def append(self , student):
        self.students.append(student)
    def get_average(self):
        total = 0
        for i in self.students:
            total += i.score
        return total / len(self.students)
    
    def get_first_by_score(self):
        best_score = self.students[0]
        
        for i in self.students:
            if i.score > best_score.score:
                best_score = i
            return best_score
        
    def get_last_by_score(self):
        last_score = self.students[0]

        for i in self.students:
            if i.score < last_score.score:
                last_score = i  
        return last_score


students = StudentList()
students.append(Student("구름" , 100))
students.append(Student("별" , 49))
students.append(Student("초코" , 81))
students.append(Student("아지" , 90))

print(students.get_average())
print(students.get_first_by_score().name)
print(students.get_last_by_score().name)


class Stack:
    def __init__(self):
        self.list = []
    def push(self,item):
        self.list.append(item)
    def pop(self):
        return self.list.pop()

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)


print(stack.pop())
print(stack.pop())
print(stack.pop())

class Queue:
    def __init__(self):
        self.list = []
    def enqueue(self,item):
        self.list.append(item)
    def dequeue(self):
        return self.list.pop(0)


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())