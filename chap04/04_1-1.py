# 연습문제 1-1
# 3명 이상 친구 이름 리스트를 작성하고 다음 내용을 프로그램하시오
# insert()로 맨 앞에 새로운 친구 추가
# insert()로 3번째 위치에 새로운 친구 추가
# append()로 마지막에 친구 추가

friends = ["철수", "영희", "민수"]

# 맨 앞에 새로운 친구 추가
friends.insert(0, "지수")

# 3번째 위치에 새로운 친구 추가
friends.insert(2, "수빈")

# 마지막에 친구 추가
friends.append("하늘")

print(friends)
