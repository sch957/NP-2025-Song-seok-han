# 하나의 숫자를 전달받아 숫자의 자리 합을 구하는 함수를 작성
# 예: 123 → 1+2+3 = 6


def digit_sum(n):
    return sum(int(digit) for digit in str(n))

result = digit_sum(123)
print(result)  # 출력: 6

