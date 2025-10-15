# 두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성. 두 개의 문자열이 같으면 -1을 반환




def first_diff_index(str1, str2):
    min_len = min(len(str1), len(str2))
    
    for i in range(min_len):
        if str1[i] != str2[i]:
            return i  # 처음 다른 위치 반환
    
    if len(str1) != len(str2):
        return min_len  # 앞부분은 같지만 길이가 다를 경우
    
    return -1  # 완전히 같을 경우


print(first_diff_index("hello", "heLlo"))  # 출력: 2
print(first_diff_index("python", "python"))  # 출력: -1
print(first_diff_index("abc", "abcdef"))  # 출력: 3
print(first_diff_index("abcde", "abfde"))  # 출력: 2
