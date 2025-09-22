# 연습문제 2-3
# 500만원을 년이율 5%로 복리 저금했을 때 5년 후의 원리금의 합계를 출력하는 프로그램

principal = 5000000  # 원금 500만원
rate = 0.05          # 연이율 5%
years = 5            # 기간 5년

amount = principal * (1 + rate) ** years

print(f"5년 후 원리금 합계: {int(amount)}원")
