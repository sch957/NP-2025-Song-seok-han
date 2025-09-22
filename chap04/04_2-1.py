# 연습문제 2-1

# for 루프를 이용하여 다음과 같은 리스트를 생성하라.
# 0~49까지의 수로 구성되는 리스트
# 1~50까지 수의 제곱으로 구성되는 리스트

# 0~49까지의 수로 구성되는 리스트
numbers = [i for i in range(50)]

# 1~50까지 수의 제곱으로 구성되는 리스트
squares = [i**2 for i in range(1, 51)]

print(numbers)
print(squares)
