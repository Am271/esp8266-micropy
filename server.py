import socket

addr = ('192.168.1.115', 6755)
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(addr)
print('Listening...')
while True:
	serv.listen(0)
	conn, addr = serv.accept()
	print('Connected by ' + str(addr))
	conn.close()