# 연습문제 6-4

#Password_manager 클래스를 작성하라. 
# 이 클래스는 사용자의 모든 과거 패스워드를 저장하는 old_passwords 리스트 변수를 갖는다. 
# 리스트의 마지막 요소는 현재 패스워드이다. 현재 패스워드를 알려주는 get_password와 
# 새로운 패스워드를 설정하는 set_password 메소드를 정의하라. 
# set_password는 과거에 사용하지 않은 새로운 패스워드를 설정할 때만 유효하다. 
# 문자열을 입력받아 현재 패스워드와 같은지 True 또는 False를 반환하는 is_correct 메소드를 정의하라.



class Password_manager:
    def __init__(self, init_password):
        # 모든 과거 패스워드 저장 (초기 비밀번호 포함)
        self.old_passwords = [init_password]

    def get_password(self):
        # 현재 패스워드 반환 (리스트 마지막 요소)
        return self.old_passwords[-1]

    def set_password(self, new_password):
        # 새로운 비밀번호가 과거에 사용된 적 없으면 추가
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            print("새로운 패스워드가 설정되었습니다.")
        else:
            print("이미 사용했던 패스워드는 사용할 수 없습니다.")

    def is_correct(self, password):
        # 현재 비밀번호와 같은지 검사
        return password == self.get_password()


# 실행
pm = Password_manager("1234")
print("현재 비밀번호:", pm.get_password())

pm.set_password("abcd")     # 새로운 비밀번호 설정
print("현재 비밀번호:", pm.get_password())

pm.set_password("1234")     # 과거 비밀번호 → 거부

print("비밀번호 확인(맞음):", pm.is_correct("abcd"))
print("비밀번호 확인(틀림):", pm.is_correct("0000"))
