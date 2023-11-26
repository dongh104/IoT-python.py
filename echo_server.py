import socket
import _thread

def subthreadEchoFunc(cs):
     while True:
        msg = cs.recv(1024)
        cs.send(msg)
        print(msg.decode())


#소켓은 아이피와 포트로 엔트포인트를 구성한다.

#클라이언트가 접속할 아이피, 외부에서 접속할 수 있도록
# 0.0.0.0 또는 그 의미의 ""로 사용할 수 있다.
ip = ""     
port = 31200

# ls는 클라이언트와 통신하는 소켓이 아닌 연결 수신용 소켓임!
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 0.0.0.0:31200 으로 바인딩, 바인딩한 주소로 외부에서 접속할 수 있게 함
ls.bind((ip, port))

#접속 대기(기본 대기수가 아마 5개 것임)
ls.listen()

while True:
    # 클라이언트 접속 시 수락
    (cs, csAddr) = ls.accept()

    print(str(csAddr) + "에서 연결됨")

    _thread.start_new_thread(subthreadEchoFunc, (cs,))
