# 연습문제 6-9

#파이썬에서 싱글톤 패턴 구현 방법

# 싱글톤은 객체가 단 하나만 존재하도록 제한하는 디자인 패턴
# 파이썬에서는 여러 방식으로 구현 가능

# 방법 1: 클래스 변수 사용
class Singleton:
    __instance = None  # 클래스 변수로 인스턴스 저장

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:  # 아직 인스턴스가 없으면 생성
            cls.__instance = super().__new__(cls)
        return cls.__instance

a = Singleton()
b = Singleton()
print(a is b)  # True, 같은 인스턴스