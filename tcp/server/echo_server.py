import socket

HOST = '0.0.0.0'
PORT = 50002
BACKLOG = 5
BUF = 4096
ENC = 'utf-8'

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(BACKLOG)
        print(f"[에코 서버] 대기 중... {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            print(f"[접속] {addr}")
            with conn:
                while True:
                    data = conn.recv(BUF)
                    if not data:
                        print(f"[종료] {addr} (수신 없음)")
                        break
                    msg = data.decode(ENC).rstrip("\n")
                    if msg.lower() == "exit":
                        print(f"[클라이언트 종료 요청] {addr}")
                        break
                    conn.sendall((msg + "\n").encode(ENC))

if __name__ == "__main__":
    main()
