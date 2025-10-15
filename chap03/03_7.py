# 제어문 예제(반복문 안의 조건문)
  
# 숫자 맞추기 게임 프로그램  
# 1~100 사이의 난수를 만들고 사용자가 1~100 사이의 수를 입력하여 맞추는 프로그램.   
# 5회까지 맞추지 못하면 종료  



from random import randint

secret_num = randint(1, 100)
num_guesses = 0  # 시도 회수
guess = 0  # 예상 숫자

while guess != secret_num and num_guesses <= 4:
    guess = eval(input('Enter your guess (1-100): '))  # 수 입력
    num_guesses = num_guesses + 1  # 시도 횟수 증가

    if guess < secret_num:  # 정답이 클 때
        print('더 큽니다.', 5 - num_guesses, '회 남았습니다.\n')
    elif guess > secret_num:  # 정답이 작을 때
        print('더 작습니다.', 5 - num_guesses, '회 남았습니다.\n')
    else:  # 정답
        print('맞았습니다!')

if num_guesses == 5 and guess != secret_num:  # 맞추지 못한 경우
    print('당신이 졌습니다. 정답은', secret_num, '입니다')
