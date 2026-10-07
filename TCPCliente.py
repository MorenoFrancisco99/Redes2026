from socket import *
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

clave = input("Ingrese clave: ")
clientSocket.send(clave.encode())
respuesta = clientSocket.recv(1024).decode()

if respuesta != "Ok":
    print("Acceso denegado")
else:
    while True:
        sentence = input("Escriba una frase (salir para terminar): ")
        if sentence == "salir":
            break
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print("From Server: ", modifiedSentence.decode())

clientSocket.close()