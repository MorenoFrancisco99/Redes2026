from socket import *
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

clave = input("Ingrese clave: ")
clientSocket.sendto(clave.encode(), (serverName, serverPort))
respuesta, _ = clientSocket.recvfrom(2048)

if respuesta.decode() != "Ok":
    print("Acceso denegado")
else:
    while True:
        message = input("Escriba una frase: ")
        if message == "0":
            break
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode())

clientSocket.close()