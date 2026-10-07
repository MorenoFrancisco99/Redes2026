from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
autorizado = []
ClaveSecreta= "pass"

print("El servidor está listo para recibir")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    text = message.decode().lower()
  
    try:
        if clientAddress not in autorizado:
            if text == ClaveSecreta:
                autorizado.append(clientAddress)
                serverSocket.sendto("Ok".encode(), clientAddress)
            else:
                serverSocket.sendto("Clave Incorrecta".encode(), clientAddress)
            continue

        modifiedMessage = text.title()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    except Exception as e:
        serverSocket.sendto("Error fatal".encode(), clientAddress)