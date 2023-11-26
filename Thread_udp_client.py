import socket
import threading

def handler(c):
    while True:
        msg, addr = c.recvfrom(1024)
        print(msg.decode())

connection = ('localhost', 2500)
s = socket.socket(socket.AF_INET,
socket.SOCK_DGRAM)

my_id = input("ID를 입력하세요: ")
s.sendto(('['+my_id+']').encode(), connection)

cThread = threading.Thread(target=handler,
args=(s,))

cThread.daemon = True
cThread.start()
while True:
    msg = '['+my_id+']'+input()
    s.sendto(msg.encode(), connection)