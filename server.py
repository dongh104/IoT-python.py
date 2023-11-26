from socket import * 
from select import * 
import sys 

HOST = '' 
PORT = 31200
BUFSIZE = 1024 
ADDR = (HOST, PORT) 

serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(ADDR) 

serverSocket.listen(10) 
connection_list = [serverSocket] 
print("select대기중")
while connection_list: 
    try:
        read_socket, write_socket, error_socket = select(connection_list, [], [], 10) 
        for sock in read_socket: 
            if sock == serverSocket: 
                clientSocket, addr_info = serverSocket.accept() 
                connection_list.append(clientSocket) 
                print("select 목록에서 변경 감지")
                for socket_in_list in connection_list: 
                    if socket_in_list != serverSocket and socket_in_list != sock: 
                        try: 
                            tmp = "Connection Success" 
                            socket_in_list.send(tmp.encode()) 
                        except Exception as e: 
                            socket_in_list.close() 
                            connection_list.remove(socket_in_list) 
            else: 
                data = sock.recv(BUFSIZE) 
                if data: 
                    for socket_in_list in connection_list: 
                        if socket_in_list != serverSocket and socket_in_list != sock: 
                            try: 
                                socket_in_list.send(data) 
                            except Exception as e: 
                                print(e.message) 
                                socket_in_list.close() 
                                connection_list.remove(socket_in_list) 
                                continue 
                        else: 
                            print('>>>', data.decode()) 
                else: 
                    connection_list.remove(sock) 
                    sock.close() 
                    print('DISCONNECTED') 
    except : 
        serverSocket.close() 
        sys.exit() 