# while 연습문제
# 10진수를 입력 받아 2진수로 변환하여 출력하는 프로그램


n = int(input('Number: '))
result = ''  # 변환 결과 저장

# 10진수를 2로 나누어 몫이 0이 될 때까지 반복해서 나머지를 구한다
while n != 0:
    m = n % 2  # 나머지
    result = str(m) + result  # 숫자를 문자열로 변환 후 앞에 붙이기
    n = n // 2  # 몫

print("2진수 =", result)
