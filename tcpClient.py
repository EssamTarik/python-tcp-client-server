import socket

def Main():
	host = "127.0.0.1"
	port = 5000

	s = socket.socket()
	s.connect((host,port))

	message = "this is a python tcp client"
	s.send("request: " + message)
	data = s.recv(1024)
	print "response : \n" + data + "\n"
	s.close()

Main()