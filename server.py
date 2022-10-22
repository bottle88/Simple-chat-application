import socket 
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER , PORT) # A tuple 
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"



# creating a socket with name 'server'
# server = socket.socket() , and the family is IPv4 and TCP so...

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting the ADDR tuple to 'server' socket
server.bind(ADDR)


# Handle connections
def handle_clients(conn , addr):
	print(f"[NEW CONNECTION] {addr} connected..")

	# Reading the message
	connected = True
	while True:
		msg_length = conn.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)
			if msg == DISCONNECT_MESSAGE : 
				connected = false 

			print(f"[{addr}] {msg}")



# Star Listening for connections...
def start():
	server.listen()
	print(f"[LISTENING] server listening on {SERVER}")
	while True :
		# conn is the new client socket and addr is the tuple 
		conn, addr = server.accept()

		# Starting a thread for every new connection (for every loop iteration)
		thread = threading.Thread(target= handle_clients, args= (conn ,addr))
		thread.start()
		a = 5
		print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1 }")
		conn.send("Msg Received".encode(FORMAT))
	





print("[STARTING] server is starting...")
start()







