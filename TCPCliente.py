from socket import *
serverName = "localhost"   #Contiene la direccion IP onombre del host. Si utiliza nombre, llevara a cabo una busqueda DNS
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
# socket del cliente
#  el primer parámetro indica que la red subyacente está utilizando IPv4. El segundo parámetro indica que el socket es de  tipo SOCK_STREAM, lo que significa que se trata de un socket TCP 

#Inicia la conexión TCP entre el cliente y el servidor
clientSocket.connect((serverName, serverPort))
#El parámetro del método connect() es la dirección del lado de servidor de la conexión. 
# Después de ejecutarse esta línea, se lleva a cabo el proceso de acuerdo en tres fases y se establece una conexión TCP entre el cliente y el servidor

clave = input("Ingrese clave: ")
clientSocket.send(clave.encode())
# envia la cadena a través del socket de cliente y la conexión TCP. 
# Observe que el programa no crea explícitamente un paquete y asocia la dirección de destino al paquete, como sucedía en el caso de los sockets UDP. 
#En su lugar, el programa cliente simplemente coloca los bytes de la cadena sentence en la conexión TCP. 
# El cliente espera entonces a recibir los bytes procedentes del servidor

respuesta = clientSocket.recv(1024).decode()
# el metodo recvfrom toma como parametro el tamaño del buffer. 2048 es adecuado para practicamente todos los propositos
# los datos del paquete se colocan en la variable resspuesta. En este caso no se devielve direccion del servidor. 
if respuesta != "Ok":
    print("Acceso denegado")
else:
    while True:
        sentence = input("Escriba una frase: ")
        if sentence == "0":
            break
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print("From Server: ", modifiedSentence.decode())

clientSocket.close()
#Esta última línea cierra el socket y, por tanto, la conexión TCP entre el cliente y el servidor.  
# Esto hace que TCP en el cliente envíe un mensaje TCP al proceso TCP del servidor 