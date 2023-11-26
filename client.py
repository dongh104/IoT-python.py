from socket import * 
from select import select 
import sys 

HOST = '127.0.0.1' 
PORT = 31200 
BUFSIZE = 1024 
ADDR = (HOST, PORT) 
clientSocket = socket(AF_INET, SOCK_STREAM)  
try: 
    clientSocket.connect(ADDR) 
except Exception as e: 
    print('Server is not found') 
    sys.exit() 
print("Connection")
def prompt(): 
    sys.stdout.write('>>>') 
    sys.stdout.flush() 
while True: 
    try:  
        connection_list = [clientSocket] 
        read_socket, write_socket, error_socket = select(connection_list, [], [], 10) 
        for sock in read_socket: 
            if sock == clientSocket: 
                clientSocket.send('Hello Server'.encode()) 
                data = sock.recv(BUFSIZE) 
                if not data: 
                    print("DISCONNECTED")
                    clientSocket.close() 
                    sys.exit() 
                else: 
                    prompt() 
        message = sys.stdin.readline() 
        clientSocket.send(message.encode()) 
        prompt() 
    except KeyboardInterrupt: 
        clientSocket.close() 
        sys.exit() 