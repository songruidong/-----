import socket
import time,threading
import random
class Light(object):
    temperature=None#温度
    humidity=None#湿度
    illumination=None#环境照度显示
    workstate=None
    workaddress=None
    name=None
    mysocket=None
    def __init__(self,name,workaddress):
        self.name=name
        self.workaddress=workaddress
        self.mysocket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # self.mysocket.connect(('127.0.0.1', 8888))

    def flush(self):
        print("begin")
        n=0
        while(True):
            self.temperature=random.randint(0,50)
            self.humidity=random.randint(0,20)
            self.illumination=random.randint(100,200)
            n+=1
            print(n)
            self.mysocket.sendto((self.temperature, self.humidity, self.illumination).__str__().encode('utf-8'),('127.0.0.1', 8888))
            time.sleep(10)
        pass
    def openorclose(self):
        while True:
            # d=self.mysocket.recv(1024)
            d, addr = self.mysocket.recvfrom(1024)
            print('Received from %s:%s.' % addr)
            if d:
                choice=d.decode('utf-8') 
                if (choice=="我准备控制你了"):
                    self.mysocket.sendto("同意".encode('utf-8'),addr)
                    print("同意")
                    time.sleep(1)
                if(choice=="关灯"):
                    self.mysocket.sendto("收到".encode('utf-8'),addr)
                    self.workstate=False
                    print("收到")
                    time.sleep(1)
                if(choice=="开灯"):
                    self.mysocket.sendto("收到".encode('utf-8'),addr)
                    self.workstate=True
                    print("收到")
                    time.sleep(1)
    def run(self):    
        t1=threading.Thread(target=self.flush,name=self.name+"flush")
        t1.start()
        t2=threading.Thread(target=self.openorclose,name=self.name+"openorclose")
        t2.start()
        time.sleep(20)
if __name__ == "__main__":
    a=Light("test","testt")
    a.run()