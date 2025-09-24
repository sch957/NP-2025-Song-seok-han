# 연습문제 6-7

# 다음 Person 클래스를 상속 받는 Employee 클래스를 정의하라. 
# Employee 클래스에 employeeID 속성을 추가하고 getID() 메소드를 정의하라. 
# getID() 메소드는 employeeID를 반환하는 메소드이다. 
# Employee 클래스를 이용하여 Employee("동양", 65, 2019)로 생성된 객체의 이름, 나이, ID 를 출력하라.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)


# Employee 클래스 (Person 상속)
class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)   # 부모 클래스 초기화
        self.employeeID = employeeID # 새로운 속성 추가

    def getID(self):
        print(self.employeeID)


# 실행
emp = Employee("동양", 65, 2019)
emp.getName()   # 이름 출력
emp.getAge()    # 나이 출력
emp.getID()     # ID 출력
