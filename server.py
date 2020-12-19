import socket

addr = ('192.168.1.115', 6755)
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(addr)
print('Listening...')
iplist = []
while True:
	serv.listen(0)
	conn, addr = serv.accept()
	if addr[0] not in iplist:
		print('Connected by ' + str(addr))
		iplist.append(addr[0])
	print('Ready to receive...')
	data = conn.recv(1024)
	print(data.decode('utf-8'))
	conn.close()