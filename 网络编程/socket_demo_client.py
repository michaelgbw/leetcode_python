import socket,sys
import time


messages = ['10','5','end']
server_address = ('localhost', 9998)
 
# 创建100个 TCP/IP socket实例
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(5)]
 
# 连接服务端
print('connecting to %s port %s' % server_address)
for s in socks:
    s.connect(server_address)
 
for message in messages:
 
    # 发送消息至服务端
    for s in socks:
        print('%s: sending "%s"' % (s.getsockname(), message) )
        s.send(bytes(message, encoding='utf8'))
 
    # 从服务端接收消息
    for s in socks:
        data = s.recv(1024)
        print( '%s: received "%s"' % (s.getsockname(), data) )
        if not data:
            print(sys.stderr, 'closing socket', s.getsockname() )
    time.sleep(1)