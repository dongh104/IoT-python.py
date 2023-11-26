import socket
import select

ip = ""
port = 31200


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.bind((ip, port))
ls.listen(5)


sock_list = []
#w_list = []
#e_list = []

sock_list.append(ls)


print("select대기중")
r_sock, w_sock, e_sock = select.select(sock_list, [], [])
print("select 목록에서 변경 감지")

for s in r_sock:
    if s == ls:
        cs, addr = ls.accept()
        print(addr)

        sock_list.append(cs)
    else: #리스닝 소켓이 아닌 경우 클라이언트 소켓으로 처리함
        msg = s.recv(1024)
        s.send(msg)
        print(msg.decode())