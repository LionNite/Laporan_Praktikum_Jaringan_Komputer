from socket import *

serverPort = 8080

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(1)

print('The server is ready to receive')

running = True
while running:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode()
	print(f"Received from {addr}: {sentence}")
	if sentence.strip().upper() == "EXIT":
		connectionSocket.send("Server shutting down...".encode())
		connectionSocket.close()
		running = False
		break
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence.encode())
	connectionSocket.close()

serverSocket.close()