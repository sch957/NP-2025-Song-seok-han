# 두 개의 매개변수 n, m을 전달받아 m x n개의 * 상자를 출력하는 프로그램을 함수로 작성
# 예: 2, 4 →    ****
#               ****


def print_star_box(n, m):
    for _ in range(m):         # m줄 반복
        print('*' * n)         # 각 줄에 n개의 * 출력

print_star_box(4, 2)
