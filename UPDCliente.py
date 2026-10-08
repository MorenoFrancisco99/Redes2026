from socket import *

serverName = "localhost" #Contiene la direccion IP onombre del host. Si utiliza nombre, llevara a cabo una busqueda DNS
serverPort = 12000 

#Creacion de socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
#AF_INET indica que la red subyacente usa IPV4.
#SOCK_DGRAM especifica que se trata de un socket UPD

clave = input("Ingrese clave: ")
clientSocket.sendto(clave.encode(), (serverName, serverPort))
#encode cambia la cadena a bytes, que es lo que toma el socket. 
#sendto asocia la direccion de destino al mensaje y envia el paquete resultante por el socket

#Captura de respuesta
respuesta, serverAddress = clientSocket.recvfrom(2048)
# el metodo recvfrom toma como parametro el tamaño del buffer. 2048 es adecuado para practicamente todos los propositos
# los datos del paquete se colocan en la variable respuesta (mensaje modificado) y la dirección de origen del paquete se almacena en la variable serverAddress. 

if respuesta.decode() != "Ok":
    #decode convertierte los bytes en cadena
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
# Esta línea cierra el socket y el proceso termina.
