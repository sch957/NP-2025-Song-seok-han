# 반지름을 전달하면 원의 면적을 반환하는 cir_area(r) 함수와
# 원의 둘레를 반환하는 cir_cirm(r) 함수를 작성하라. 이들 함수를
# 이용하여 반지름이 3.5cm인 원의 면적과 둘레를 소수점 아래
# 첫 자리까지 구하라.

import math

# 원의 면적을 구하는 함수
def cir_area(r):
    return math.pi * r ** 2

# 원의 둘레를 구하는 함수
def cir_cirm(r):
    return 2 * math.pi * r

# 반지름
radius = 3.5

# 계산
area = cir_area(radius)
circumference = cir_cirm(radius)

# 결과 출력 (소수점 첫째 자리까지)
print(f"반지름이 {radius}cm인 원의 면적: {area:.1f} cm²")
print(f"반지름이 {radius}cm인 원의 둘레: {circumference:.1f} cm")
