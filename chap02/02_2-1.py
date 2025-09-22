# 연습문제 2-1
# 초를 입력하면 분과 초로 표시하는 프로그램. 예를 들어, 200초를 입력하면 3분 20초로 표현하라

seconds = int(input("초를 입력하세요: "))

minutes = seconds // 60
remaining_seconds = seconds % 60

print(f"{minutes}분 {remaining_seconds}초")
