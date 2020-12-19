# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine, time
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc, socket
import webrepl
gc.collect()
#machine.freq(160000000)

def getCred():
	f = open('credentials.txt')
	x = f.read().split()
	f.close()
	return x[0], x[1]

def sendInfo():
	c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		c.connect(('192.168.1.115', 6755))
	except:
		pass
	time.sleep_ms(200)
	del c

def do_connect():
	import network
	sta_if = network.WLAN(network.STA_IF)
	if not sta_if.isconnected():
		print('connecting to network...')
		ssid, passw = getCred()
		sta_if.active(True)
		sta_if.connect(ssid, passw)
	while not sta_if.isconnected():
		pass

def start():
	spi = machine.SPI(1, baudrate=4000000, polarity=0, phase=0)
	ss = machine.Pin(5, machine.Pin.OUT)
	ss.value(0)
	read(spi)

def read(spi):
	databuff = bytearray(512)
	a = databuff[0]
	spiServ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	spiServ.connect(('192.168.1.115', 6755))
	while databuff[0] == a:
		spi.readinto(databuff)
	db = ''
	for i in databuff:
		# print(chr(i), end='')
		db = chr(i) + db
	print(db)
	data = bytes(db, 'utf-8')
	spiServ.send(data)



do_connect()
webrepl.start()
sendInfo()
start()