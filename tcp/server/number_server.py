import socket

HOST = '0.0.0.0'
PORT = 50003
BACKLOG = 5
BUF = 1024
ENC = 'utf-8'

def sum_1_to_n(n: int) -> int:
    # 등차수열 합 공식 사용
    return n * (n + 1) // 2

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(BACKLOG)
        print(f"[숫자 서버] 대기 중... {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            print(f"[접속] {addr}")
            with conn:
                try:
                    data = conn.recv(BUF)
                    if not data:
                        print(f"[종료] {addr} (수신 없음)")
                        continue
                    txt = data.decode(ENC).strip()
                    n = int(txt)
                    result = sum_1_to_n(n)
                    resp = str(result) + "\n"
                    print(f"[요청] {addr} n={n} -> 합={result}")
                    conn.sendall(resp.encode(ENC))
                except Exception as e:
                    print(f"[에러] {addr} {e}")
                    conn.sendall(b"ERROR\n")

if __name__ == "__main__":
    main()
