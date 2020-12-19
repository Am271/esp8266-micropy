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

do_connect()
webrepl.start()
sendInfo()