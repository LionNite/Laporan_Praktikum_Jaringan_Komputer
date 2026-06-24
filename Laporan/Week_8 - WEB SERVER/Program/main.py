from socket import *
import sys
import os

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', 6789))
serverSocket.listen(1)

while True:
	print('Ready to serve...')
	print('Access on http://127.0.0.1:6789')
	connectionSocket, addr = serverSocket.accept()

	try:
		message = connectionSocket.recv(1024).decode()
		filename = message.split()[1]

		if filename == '/':
			filename = '/index.html'

		filepath = filename[1:]

		if not os.path.exists(filepath):
			filepath = '404.html'
			status = 'HTTP/1.1 404 Not Found\r\n'
		else:
			status = 'HTTP/1.1 200 OK\r\n'

		with open(filepath, 'r', encoding='utf-8') as f:
			outputdata = f.read()

		header = status + 'Content-Type: text/html\r\n\r\n'
		connectionSocket.send(header.encode())
		connectionSocket.send(outputdata.encode())

		connectionSocket.close()

	except Exception:
		connectionSocket.send('HTTP/1.1 500 Internal Server Error\r\n\r\n'.encode())
		connectionSocket.close()

serverSocket.close()
sys.exit()