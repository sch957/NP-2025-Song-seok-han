# 숫자를 전달받아 그 수의 약수를 리스트로 반환하는 함수를 작성



def get_divisors(n):
    divisors = []              # 약수를 저장할 리스트
    for i in range(1, n + 1):  # 1부터 n까지 반복
        if n % i == 0:         # 나누어 떨어지면
            divisors.append(i) # 약수로 추가
    return divisors


print(get_divisors(12))  # [1, 2, 3, 4, 6, 12]
