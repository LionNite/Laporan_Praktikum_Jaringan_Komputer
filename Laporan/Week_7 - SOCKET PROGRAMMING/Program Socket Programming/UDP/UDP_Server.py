from socket import *

serverPort = 8070

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print('The server is ready to receive')

running = True
while running:
	message, clientAddress = serverSocket.recvfrom(2048)
	decoded_message = message.decode()
	print(f"Received from {clientAddress}: {decoded_message}")
	if decoded_message.strip().upper() == "EXIT":
		serverSocket.sendto("Server shutting down...".encode(), clientAddress)
		running = False
		break
	modifiedMessage = decoded_message.upper()
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)

serverSocket.close()