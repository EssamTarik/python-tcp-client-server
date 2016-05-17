import socket

def Main():
	host = '127.0.0.1'
	port = 5000	
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "socket created"
	s.bind((host,port))
	print "socket binded"
	
	s.listen(1)
	c, addr = s.accept()
	print "connection from %s " %str(addr)
	
	while (True):
#		data = c.recv(1024)
#		if not data:
#			break
#		print str(data)
		print c.recv(512)
		try:
			data = "HTTP/1.1 200 OK\nContent-Type: text/html\n\nthis is a python tcp server"
			c.sendall(data)
			c.close()
			break
		except Exception,e:
			print str(e)
	
	s.shutdown(1)
	s.close()
Main()
