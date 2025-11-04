import socket

HOST = '127.0.0.1'  # 필요 시 WSL IP로 변경
PORT = 50001
BUF = 1024

def main():
    with socket.create_connection((HOST, PORT)) as s:
        data = s.recv(BUF)
        print("[서버시간]", data.decode())

if __name__ == "__main__":
    main()
