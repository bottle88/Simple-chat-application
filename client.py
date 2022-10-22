import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER , PORT) # A tuple 
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
	message = msg.encode(FORMAT) # datatype - encoded string

	# Length of the 'message'
	message_length = len(message) # datatype - int
	send_length = str(message_length).encode(FORMAT) # datatype- enocded string

	# len(send_length) - dataype = int
	# Fill it to 64 bytes
	send_length += b' '*(HEADER - len(send_length)) 

	# Sending data to server
	client.send(send_length)
	client.send(message)

	print(client.recv(2048).decode(FORMAT))


send("Hello , am I connected?")
input()
send("Hello everyone")
input()
send(DISCONNECT_MESSAGE)

#user = input("Enter Something:")
#send(user)
#input()


""" Suggestions :
	1. Code Logic
	2. Client to Client
	3. Clean output
	4. Over LAN
	4. Over WAN
"""



