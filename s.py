import socket
HOST = '127.0.0.1'
PORT = 2500

num = int(input("숫자를 입력하세요 : "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(str(num).encode())

    msg = s.recv(1024)
    print("Result : ", msg.decode())