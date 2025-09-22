# 연습문제 2-5
# 판매자가 딸기와 포도를 판매하고 있다. 포도 한 알의 무게는 75g이고 딸기 한 알의 무게는 
# 113.5g이다. 사용자로부터 포도 알의 개수와 딸기의 개수를 입력 받아 총 무게를 계산하여 출력하는 
# 프로그램을 작성하고 실행하라

grape_count = int(input("포도 알 개수 입력: "))
strawberry_count = int(input("딸기 알 개수 입력: "))

grape_weight = 75       # 포도 한 알 무게(g)
strawberry_weight = 113.5  # 딸기 한 알 무게(g)

total_weight = grape_count * grape_weight + strawberry_count * strawberry_weight

print(f"총 무게: {total_weight}g")
