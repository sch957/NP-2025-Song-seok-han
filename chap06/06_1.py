# 연습문제 6-3
# Moneybox 클래스를 작성하라. 
# 이 클래스는 저축한 총액을 저장하는 인스턴스 변수가 있다.
# deposit(money) 메서드는 인수로 주어진 금액만큼 저축하고 총액을 출력한다,
# extract(money) 메소드는 money를 인출하고 총액을 출력한다. get_total() 메소드는 총액을 알려준다.

# my_money = Moneybox() 객체를 생성하고 1000원을 저축하고, 200원을 인출한 다음, 총액을 출력하라.


# Moneybox 클래스 정의
class Moneybox:
    def __init__(self):
        self.total = 0   # 저축 총액 저장

    def deposit(self, money):
        self.total += money
        print(f"{money}원이 입금되었습니다. 총액: {self.total}원")

    def extract(self, money):
        if money > self.total:
            print("잔액이 부족합니다.")
        else:
            self.total -= money
            print(f"{money}원이 인출되었습니다. 총액: {self.total}원")

    def get_total(self):
        return self.total


# 실행
my_money = Moneybox()
my_money.deposit(1000)     # 1000원 저축
my_money.extract(200)      # 200원 인출
print("최종 총액:", my_money.get_total())  # 총액 출력
