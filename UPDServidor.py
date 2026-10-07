from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
# crea también un socket de tipo SOCK_DGRAM (un socket UDP)

serverSocket.bind(("", serverPort))
# asigna el número de puerto 12000 al socket del servidor

autorizado = []
ClaveSecreta= "pass"

print("El servidor está listo para recibir")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    # los datos del paquete se almacenan en la variable message y la dirección de  origen del paquete  se coloca en la variable clientAddress
    # La variable clientAddress contiene tanto la dirección IP del cliente como el número de puerto del cliente.
    #Esta es la informacion de retorno


    text = message.decode().lower()
    #decode convertierte los bytes en cadena

    try:
        if clientAddress not in autorizado:
            if text == ClaveSecreta:
                autorizado.append(clientAddress)
                serverSocket.sendto("Ok".encode(), clientAddress)
                #Esta última línea asocia la dirección del cliente (dirección IP y número de puerto) al mensaje escrito y envía el paquete resultante al socket del servidor.
                #encode cambia la cadena a bytes, que es lo que toma el socket. 

            else:
                serverSocket.sendto("Clave Incorrecta".encode(), clientAddress)
            continue

        modifiedMessage = text.title()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    except Exception as e:
        serverSocket.sendto("Error fatal".encode(), clientAddress)
#permanece en el bucle while, esperando la llegada de otro paquete UDP