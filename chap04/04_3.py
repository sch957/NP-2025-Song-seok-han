# 연습문제 3 (딕셔너리)

# 다음 딕셔너리에 대해 물음에 답하라. 
# days = {'January':31, 'February':28, 'March':31, 'April':30,
# 'May':31, 'June':30, 'July':31, 'August':31,
# 'September':30, 'October':31, 'November':30, 'December':31}

# 사용자가 월을 입력하면 해당 월에 일수를 출력하라
# 알파벳 순서로 모든 월을 출력하라
# 일수가 31인 월을 모두 출력하라
# 월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력하라
# 사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)


days = {'January':31, 'February':28, 'March':31, 'April':30,
        'May':31, 'June':30, 'July':31, 'August':31,
        'September':30, 'October':31, 'November':30, 'December':31}

# 1. 사용자가 월을 입력하면 해당 월에 일수 출력
month = input("월 입력: ")
if month in days:
    print(f"{month}의 일수: {days[month]}")
else:
    print("잘못된 월입니다.")

# 2. 알파벳 순서로 모든 월 출력
print(sorted(days.keys()))

# 3. 일수가 31인 월 출력
months_31 = [m for m, d in days.items() if d == 31]
print(months_31)

# 4. 월의 일수를 기준으로 오름차순으로 (key-value) 쌍 출력
sorted_by_days = sorted(days.items(), key=lambda x: x[1])
print(sorted_by_days)

# 5. 사용자가 월을 3자리만 입력하면 일수 출력
abbr = input("월 3자리 입력 (예: Jan, Feb): ")
abbr_to_full = {m[:3]: m for m in days.keys()}
if abbr in abbr_to_full:
    full_month = abbr_to_full[abbr]
    print(f"{full_month}의 일수: {days[full_month]}")
else:
    print("잘못된 월 약어입니다.")
