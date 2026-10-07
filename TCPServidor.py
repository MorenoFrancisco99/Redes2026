from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
# socket del server
#  el primer parámetro indica que la red subyacente está utilizando IPv4. El segundo parámetro indica que el socket es de  tipo SOCK_STREAM, lo que significa que se trata de un socket TCP 

serverSocket.bind(("", serverPort))
# asigna el número de puerto 12000 al socket del servidor

serverSocket.listen(1)
#Esta línea hace que el servidor esté a la escucha de solicitudes de conexión TCP del cliente. 
# El parámetro especifica el número máximo de conexiones en cola (al menos, 1).


ClaveSecreta = "pass"
print("El servidor está listo para recibir")

while True:
    connectionSocket, addr = serverSocket.accept()
    #Cuando un cliente llama a esta puerta, el programa invoca el método accept() para el serverSocket, 
    #el cual crea un nuevo socket en el servidor, denominado  connectionSocket, dedicado a este 
    #cliente concreto. El cliente y el servidor completan entonces el acuerdo en tres fases, creando una 
    #conexión TCP entre el socket clientSocket del cliente y el socket connectionSocket del 
    #servidor. Con la conexión TCP establecida, el cliente y el servidor ahora pueden enviarse bytes entre 
    #sí a través de la misma. Con TCP, no solo está garantizado que todos los bytes enviados desde un 
    #lado llegan al otro lado, sino que también queda garantizado que llegarán en orden.

    clave = connectionSocket.recv(1024).decode()
    # el metodo recvfrom toma como parametro el tamaño del buffer. 2048 es adecuado para practicamente todos los propositos
    # los datos del paquete se colocan en la variable resspuesta. En este caso no se devielve direccion del servidor. 

    if clave.lower() != ClaveSecreta:
        connectionSocket.send("Clave Incorrecta".encode())
        # envia la cadena a través del socket de server y la conexión TCP. 
        # Observe que el programa no crea explícitamente un paquete y asocia la dirección de destino al paquete, como sucedía en el caso de los sockets UDP. 
        #En su lugar, el programa cliente simplemente coloca los bytes de la cadena sentence en la conexión TCP. 

        connectionSocket.close()
         # se cierra el socket de conexión. 
         # Pero puesto que serverSocket permanece abierto, otro cliente puede llamar a la puerta y enviar 
         # una frase al servidor para su modificación.

        continue
    connectionSocket.send("Ok".encode())

    while True:
        data = connectionSocket.recv(1024)
        if not data: 
            break
        connectionSocket.send(data.decode().title().encode())
    connectionSocket.close()