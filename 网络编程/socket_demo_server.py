# -*- coding:utf-8 -*-
import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock,mask):
    #接受客户端创建实例
    conn,addr = sock.accept()
    print("accepted",conn,'from',addr)
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,readData)  #新连接注册read回调函数

def readData(conn,addr):
    #接受数据
    data = conn.recv(1024)
    print(type(conn))
    if data:
        print("print",repr(data),'to',conn)
        conn.send(data)
    else:
        print("closing",conn)
        sel.unregister(conn)
        conn.close()



server = socket.socket()
server.bind(('localhost',9998))
server.listen(500)
server.setblocking(False)
sel.register(server,selectors.EVENT_READ,accept)  #注册事件，只要来一个连接就调accept这个函数,


while True:
    events = sel.select()  #这个select,看起来是select，有可能调用的是epoll，看你操作系统是Windows的还是Linux的,默认阻塞，有活动连接就返回活动连接列表
    print("事件：",events)
    for key,mask in events:
        callback = key.data #相当于调accept了
        callback(key.fileobj,mask)  #key.fileobj=文件句柄
