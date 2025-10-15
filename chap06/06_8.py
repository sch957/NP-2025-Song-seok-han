# 연습문제 6-8

# 앞의 Person 클래스에서 새로운 Person 객체가 생성될 때 ID를 1001번지부터 순차적으로 
# 자동으로 부여할 수 있도록 Employee 클래스를 포함해서 변경하시오. 새로운 Employee객체를 
# 만들어 getId() 를 호출할 때 Id가 중복되면 안된다.

class Person:
    # 클래스 변수 (모든 인스턴스가 공유)
    count = 1000  

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1  # 객체 생성 시마다 1 증가
        self.__id = Person.count

    def getId(self):
        print(self.__id)

    def getAge(self):
        print(self.age)


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)  # 부모 생성자 호출
        self.position = position

    def getPosition(self):
        print(self.position)


# 테스트 코드
p1 = Person("홍길동", 20)
p2 = Person("김철수", 22)
e1 = Employee("이영희", 25, "개발자")
e2 = Employee("박민수", 30, "디자이너")

p1.getId()  # 1001
p2.getId()  # 1002
e1.getId()  # 1003
e2.getId()  # 1004
