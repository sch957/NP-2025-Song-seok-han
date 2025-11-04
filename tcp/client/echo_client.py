import socket

HOST = '127.0.0.1'
PORT = 50002
ENC = 'utf-8'

def main():
    with socket.create_connection((HOST, PORT)) as s:
        print("메시지를 입력하세요. 종료하려면 'exit'")
        while True:
            msg = input("> ")
            s.sendall((msg + "\n").encode(ENC))
            if msg.lower() == "exit":
                break
            data = s.recv(4096)
            print("에코:", data.decode(ENC).rstrip("\n"))

if __name__ == "__main__":
    main()
