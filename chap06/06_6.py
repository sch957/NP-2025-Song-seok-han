# 연습문제 6-10

#  동물(Animal)을 울음을 추상 메소드로 하는 추상클래스로 정의하고,
# 개(Dog)와 고양이(Cat)를 구체적인 클래스로 정의한 후,
# 각 동물의 울음소리를 출력하는 프로그램을 작성하시오.
# 각 동물객체는 자신의 이름을 속성으로 가지며,
# 생성자에서 이름을 초기화합니다.
# 추가적으로 Animal 클래스는 현재 생성된 동물 객체의 수를 클래스 변수로 가지고,
# 정적 메소드로 현재 동물 객체의 수를 반환하는 메소드를 구현
# 객체가 생성(__init__)될 때 객체의 수를 증가하고 삭제(__del__(self) ) 될 때 객체의 수를 감소

# 테스트
# 개나 고양이 객체들을 리스트로 생성하고 개나 Animal 변수로 받아 동적 바인딩이 되는지 확인하시오.
# 모든 객체들이 울게 하는 함수를 작성하여 테스트하시오

from abc import ABC, abstractmethod

class Animal(ABC):
    animal_count = 0  # 클래스 변수 (동물 객체 수)

    def __init__(self, name):
        self.name = name
        Animal.animal_count += 1  # 객체 생성 시 개수 증가

    def __del__(self):
        Animal.animal_count -= 1  # 객체 삭제 시 개수 감소

    @abstractmethod
    def sound(self):
        pass

    @staticmethod
    def get_animal_count():
        return Animal.animal_count


# Dog 클래스
class Dog(Animal):
    def sound(self):
        return "멍멍"


# Cat 클래스
class Cat(Animal):
    def sound(self):
        return "야옹"


# 개별 동물 울음 출력 함수
def animal_sound(animal: Animal):
    print(animal.sound())

# 여러 동물 울음 출력 함수
def animal_sounds(animal_list: list[Animal]):
    for a in animal_list:
        print(a.sound())


# 테스트 코드
if __name__ == "__main__":
    dog: Dog = Dog("바둑이")
    print(dog.sound())  # Output: 멍멍

    cat = Cat("야옹이")
    print(cat.sound())  # Output: 야옹

    any: Animal = Dog("바둑이2")
    print(any.sound())  # Output: 멍멍

    any: Animal = Cat("야옹이2")
    print(any.sound())  # Output: 야옹

    alist: list[Animal] = [Dog("바둑이a"), Cat("나비b"), Dog("멍멍이c"), Cat("야옹이d")]
    print(alist)  # 객체 리스트 출력 (메모리 주소 형태)

    animal_sound(alist[2])      # 멍멍
    animal_sounds(alist)        # 전체 동물 울음 출력

    print(f"총 동물의 수: {Animal.get_animal_count()}")  # 8

    # 올바른 객체 삭제
    del dog
    del cat

    print(f"총 동물의 수: {Animal.get_animal_count()}")  # 6
