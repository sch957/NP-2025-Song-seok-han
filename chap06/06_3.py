# 연습문제 6-5

# Articles 클래스를 작성하라. 
# 이 클래스는 각각 제품의 이름, 재고 수량, 단가를 나타내는name, stock, price 인스턴스 변수를 가지고 있다. 
# offer_price() 메소드는 구매 수량을 인수로 전달받아 총 가격을 반환한다. 
# 구매 수량이 1~10개 이하이면 정상 가격을 반환하고, 11~50개이면 5% 할인된 가격을 반환한다. 
# 또 51개 이상이면 10% 할인해 준다. purchase() 메소드는 구매 수량을 인수로 전달받아 재고 수량을 구매 수량만큼 감소한다.

# 이 클래스를 이용하여 단가 1000원인 ”mask“를 10,000장으로 설정하고, 40장 구매 가격과 구매 후 재고를 출력하라.




class Articles:
    def __init__(self, name, stock, price):
        self.name = name      # 제품 이름
        self.stock = stock    # 재고 수량
        self.price = price    # 단가

    def offer_price(self, quantity):
        # 할인 규칙에 따른 총 가격 계산
        if 1 <= quantity <= 10:
            return self.price * quantity
        elif 11 <= quantity <= 50:
            return int(self.price * quantity * 0.95)  # 5% 할인
        elif quantity >= 51:
            return int(self.price * quantity * 0.90)  # 10% 할인
        else:
            return 0  # 잘못된 수량

    def purchase(self, quantity):
        if quantity > self.stock:
            print("재고가 부족합니다.")
            return None
        else:
            self.stock -= quantity
            return self.stock


# 실행 
mask = Articles("mask", 10000, 1000)   # 이름, 재고, 단가
price = mask.offer_price(40)           # 40장 구매 가격
mask.purchase(40)                      # 재고 감소

print("40장 구매 가격:", price, "원")
print("구매 후 남은 재고:", mask.stock, "장")
