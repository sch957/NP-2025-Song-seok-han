import socket

HOST = '127.0.0.1'
PORT = 50003
ENC = 'utf-8'

def main():
    n = input("정수 n을 입력하세요: ").strip()
    with socket.create_connection((HOST, PORT)) as s:
        s.sendall(n.encode(ENC))
        data = s.recv(1024)
        print("결과:", data.decode(ENC).strip())

if __name__ == "__main__":
    main()
