# 연습문제 4 (집합)
# 1부터 45까지의 수 중에서 6개를 선택하여 로또 번호를 만드는 프로그램

import random

pick = set()  # 빈 집합 생성

while len(pick) < 6:
    n = random.randint(1, 45)  # 1~45 사이 랜덤 숫자 생성
    if n not in pick:
        pick.add(n)  # 집합에 숫자 추가

print(pick)          # 선택된 로또 번호 출력 (순서 없음)
print(sorted(pick))  # 정렬된 로또 번호 출력
