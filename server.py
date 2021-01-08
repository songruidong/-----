import socket
import time,threading
class Server(object):   
    def handle(self,data,addr):

        # e=None
        # while True:
            # data=data.decode('utf-8')
            # print(type(data))
        if(type(data)!=type("aa")):
            data=str(data, "utf-8")
        print(data)
        time.sleep(1)

        if data:
            if(data=="同意"):
                if(self.e[0]>25):
                    self.mysocket.sendto("开灯".encode('utf-8'),addr)
                    print("开灯server")
                else:
                    self.mysocket.sendto("关灯".encode('utf-8'),addr)
                    print("关灯server")
            elif(data=="收到"):
                return


            else:
                self.e=tuple(eval(data))
                self.mysocket.sendto("我准备控制你了".encode('utf-8'),addr)
                print("我准备控制你了server")

                   
        # self.mysocket.close()
        # print('Connection from %s:%s closed.' % addr)

    def __init__(self):
        self.mysocket=socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
        self.mysocket.bind(('127.0.0.1', 8888))
        self.e=None
        print('Waiting for connection...')
        n=1
        while True:
            # 接受一个新连接:
            # sock, addr = self.mysocket.accept()
            data, addr = self.mysocket.recvfrom(1024)
            print(n,":")
            # print('Received from %s:%s.' % addr))
            # 创建新线程来处理TCP连接:
            t = threading.Thread(target=self.handle, args=(data, addr))
            t.start()
if __name__ == "__main__":
    a=Server()
