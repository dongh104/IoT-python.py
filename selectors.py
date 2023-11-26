import selectors
import socket

def accept(sock,mask):
    conn, addr = sock.accept()
    print('accepted', conn, 'from', addr)
    conn.setblocking(False) #논블로킹이어야 하는 이유?
    # 클라이언트 데이터 수신 시 read 함수 콜벡
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sel = selectors.DefaultSelector()

sock = socket.socket()
sock.bind(('localhost', 2500)) # ''대신 IP가 localhost일 때의 아치점?
sock.listen(100)
sock.setblocking(False)

sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)