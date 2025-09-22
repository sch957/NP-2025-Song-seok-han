# 연습문제 2-2 
# 분(min)을 입력 하면, 일, 시간, 분으로 출력하는 프로그램을 만들어라. (예 : 1550분은 1일 1시간 50분)

minutes = int(input("분을 입력하세요: "))

days = minutes // (24 * 60)
hours = (minutes % (24 * 60)) // 60
remaining_minutes = minutes % 60

print(f"{days}일 {hours}시간 {remaining_minutes}분")
