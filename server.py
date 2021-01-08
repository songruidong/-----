import socket
import time,threading
class Server(object):   
    def handle(self,sock,addr):
        print('Accept new connection from %s:%s...' % addr)
        e=None
        # sock.send(b'Welcome!')
        while True:
            data = sock.recv(1024)
            data=data.decode('utf-8')
            time.sleep(1)
            
            # if not data or data.decode('utf-8') == 'exit':
            #     break
            # sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
            if data:
                print(data)
                if(data=="同意"):
                    if(e[0]>25):
                        sock.send("开灯".encode('utf-8'))
                        print("开灯")
                    else:
                        sock.send("关灯".encode('utf-8'))
                        print("关灯")
                elif(data=="收到"):
                    continue

                
                else:
                    e=tuple(eval(data))
                    sock.send("我准备控制你了".encode('utf-8'))
                    print("我准备控制你了")

                   
        sock.close()
        print('Connection from %s:%s closed.' % addr)

    def __init__(self):
        self.mysocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mysocket.bind(('127.0.0.1', 8888))
        self.mysocket.listen(5)
        print('Waiting for connection...')
        while True:
            # 接受一个新连接:
            sock, addr = self.mysocket.accept()
            # 创建新线程来处理TCP连接:
            t = threading.Thread(target=self.handle, args=(sock, addr))
            t.start()
if __name__ == "__main__":
    a=Server()
