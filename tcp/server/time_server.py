import socket
import datetime

HOST = '0.0.0.0'
PORT = 50001
BACKLOG = 5
BUF = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(BACKLOG)
        print(f"[시간 서버] 대기 중... {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            with conn:
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[접속] {addr} -> 현재시간 전송: {now}")
                conn.sendall(now.encode())
                # 전송 후 연결 종료

if __name__ == "__main__":
    main()
