# 재귀 함수를 이용하여 1부터 100까지의 합을 계산하는 프로그램



def recursive_sum(n):
    if n == 1:                # 종료 조건
        return 1
    else:
        return n + recursive_sum(n - 1)  # 자기 자신을 호출하여 누적합 계산


print(recursive_sum(100))  # 5050
