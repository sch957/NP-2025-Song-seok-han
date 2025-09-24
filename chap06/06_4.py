# 연습문제 6-6

# 다음 프로그램을 실행했을 때 아래 내용이 출력되도록 클래스를 정의하라. 
# 학번(id) 앞 4자리가 2018보다 작으면 grade() 메소드에 의해 “3학년입니다“가 출력되고 아니면 ”3학년이 아닙니다“가 출력된다.

class Student:
    def __init__(self, name, id, dept):
        self.name = name
        self.id = id
        self.dept = dept

    def grade(self):
        # 학번 앞 4자리 추출 후 학년 판정
        year = int(str(self.id)[:4])
        if year < 2018:
            print("3학년입니다")
        else:
            print("3학년이 아닙니다")


# 실행
man = Student(name="홍길동", id=20150001, dept="로봇공학과")
print("이름: {}, 학번: {}, 학과: {}".format(man.name, man.id, man.dept))
man.grade()
