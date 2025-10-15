# 조건문 예제
# 평년과 윤년 구분하는 프로그램
# 년도가 4로 나뉘어지고 100으로 나뉘어지지 않거나
# 400으로 나뉘어지면 윤년이다

year = int(input("Type a year : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
