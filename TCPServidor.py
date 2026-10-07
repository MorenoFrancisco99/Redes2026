from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
ClaveSecreta = "pass"
print("El servidor está listo para recibir")

while True:
    connectionSocket, addr = serverSocket.accept()

    clave = connectionSocket.recv(1024).decode()
    if clave.lower() != ClaveSecreta:
        connectionSocket.send("Clave Incorrecta".encode())
        connectionSocket.close()
        continue
    connectionSocket.send("Ok".encode())

    while True:
        data = connectionSocket.recv(1024)
        if not data: 
            break
        connectionSocket.send(data.decode().title().encode())
    connectionSocket.close()