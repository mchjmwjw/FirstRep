# coding=utf8
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024 # 1kb
ADDR =(HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
# udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)  # 传入请求的最大数

while True:
	print('等待连接...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('连接来自:', addr)
	
	while True:
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
		 break
		tcpCliSock.send(('[%s] %s' % (ctime(), data.decode('utf-8'))).encode('utf-8'))
	tcpCliSock.close()
	
tcpSerSock.close()