import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('127.0.0.1',2500)
s.bind(address)
s.listen(5)
while True:
    client, addr = s.accept()
    print("Connection requested from" , addr)
    temp = (client.recv(1024))
    # print(int(temp))
    num = int(temp.decode('utf-8'))
    sum = 0
    for i in range(1, num + 1) :
        sum = sum + i
    client.send(str(sum).encode())
    client.close()