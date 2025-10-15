# 문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환하는 함수를 작성



def find_char_positions(text, char):
    positions = []                        # 위치를 저장할 리스트
    for i in range(len(text)):            # 문자열 길이만큼 반복
        if text[i] == char:               # 문자가 일치하면
            positions.append(i)           # 위치(인덱스) 추가
    return positions


print(find_char_positions("banana", "a"))  # [1, 3, 5]
