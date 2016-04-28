# -*- coding: utf8 -*-

import socket

from thread import SocketIoThread


from threading import Timer  
import time  


class SocketServer:
    def __init__(self,port,IO):
        self.io = IO
        self.io.setServer(self)
        self.uid = 0
        self.port = port
        self.IoList = {}

    def mySendMessage(self):
      ##引入线程来模拟后台向前台push数据
      while 1:
        print "running"
        if self.uid:
            self.IoList[self.uid].sendData("new message")
        time.sleep(5)

    def run(self):
        myTimer=Timer(5,self.mySendMessage)
        myTimer.start()
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.bind(('',self.port))
        sock.listen(100)

        while True:
            try:
                connection,address = sock.accept()
                self.uid += 1
                self.IoList[self.uid] = SocketIoThread(connection,self.uid,self.io)
                self.IoList[self.uid].start()
            except:
		        time.sleep(1)
            
    def sendData(self,uid,text):
        if self.IoList.has_key(uid):
            print uid,text
            self.IoList[uid].sendData(text)
        


            


