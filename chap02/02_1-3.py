# 연습문제 1-3
# 원의 반지름을 입력 받아 원의 둘레와 원의 면적을 출력하는 프로그램을 작성하라

import math

r = float(input("원의 반지름을 입력하세요"))

# 둘레
cir = 2 * math.pi * r

# 면적 
area = math.pi * r ** 2


print("원의 둘레 : ", cir)
print("원의 면적 : ", area)