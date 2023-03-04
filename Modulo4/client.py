import socket
import sys
# dir(socket) ---------- para ver todos los modulos
import threading

# Primero defino una calse de servidor 

#-------------------------------#
#           SERVER              #
#-------------------------------#
class Server():
    
    # Inicilizo el constructor
    def __init__(self):
        
        # Inicializo el objeto de socket servidor
        # Le indico la familia de direcciones AF_INET, el tipo de socket STREAM (bidireccionales)
        # Podemos recibir y comunicarnos con el cliente.
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Puede fallar y lo meto todo dentro de un TRY
        try:
            #serversocket.bind((socket.gethostname(), 80))
            # La funcion BIND se encarga de verificar si el puerto que le indicamos se encuentra disponible.
            # Si esta disponible lo reserva para que el socket sea creado ene lel sistema operativo.
            # Puede ser cualquier espacio que este libre , para que pueda vincularse a esa referecia y lo va a ocupar
            # nugun otro soclet puede ocupar ese lugar.
            # 0.0.0.0 significa cualquier punto de la interface de red 
            # Nos coje el puerto 8000
            serversocket.bind(('0.0.0.0', 8000))
        except socket.error as msg:
            # SI falla el BIND es seguro porque ya esta ocupado eses espacio de la red.
            print('Bind failed. Error Code : %s Message %s ' %(str(msg[0]), str(msg[1])))
            sys.exit()
            
            
        try:
            # SI lo anterior funciono le digo que se ponga en modo de ESCUCHA
            # Esto nos permite escuchar el numero de conecciones concurrentes
            # Cuantos clientes queremos que se connecten a nosostros de forma total. 
            serversocket.listen(5)
            
            
            # UNa vez que tenemos el servidor a la escucha
            # Se mete en el bucle y no saldra hasta que se le indique lo contrario.
            # TRUE mientras s eescucha...
            while True:
                
                # Se acepta la coneccion que venga de un cliente.
                # Se escarga de aceptar una coneccion entrante por parte de un cliente
                #wait to accept a connection - blocking call
                # conn, addr = serversocket.accept()ADDRESS
                print('Connection with %s : %s ' %(addr[0], str(addr[1])))
                
                # Ahora lo que hago es inicicializar el HILO
                # Aqui meto la ejecucion de que queremos que haga el servidor cuando se connecte un cliente.
                #  EL cliente el el mismo servidor con la funcion CLIENTHREAD
                hilo = threading.Thread(target=self.clientthread, args=(conn,))
                # Le decimos que inicie el hilo
                
                # CUnado tenemos esto lo que hacemos es definir el HILO al que le pasaremos la conecion con el socket.
                # Este hilo se encargara de realizar la ejecucion que le indiquemos.
                hilo.start()
        finally:
            serversocket.close()

    def clientthread(self,conn):
        # Aqui le enviamos un mensage de bienvenida cuendo se conecte un cliente.
        # Esto funcion SEND nos pertmite enviar un paquete de datos al otro extremo de la coneccion.
        # Aqui lo ocdificamos para que sea un binary string con ENCODE
        conn.send('Welcome to the server. Type something! \n'.encode()) #send only takes string
        
        # Mientras sea lo metemos un un bucle
        while True:
            # guardamos lo que reviba la coneccion
            data = conn.recv(1024)
            
            # Le decimos al cliente que ha tenido una coneccion exitosa devolvinedole el mismo mensage con un OK
            reply = 'OK...' + str(data)
            
            # Si no hay datos rompemos el bucle
            if not data:
                break
            
            
            # Si la trama tienen datos le enviamos el reply codificado
            conn.sendall(reply.encode())
        # FInamente cerramos la coneccion.
        conn.close()

#-------------------------------#
#           CLIENT              #
#-------------------------------#
class Client():
    
    # Inicializo el constructor
    def __init__(self):
        
        # Primero se crea el objeto
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # La coneccion puede ser TCO o UDP y 
        # seleccionamos el dominio del servidor al que nos queremos connectar y el puerto
        # Esto realiza la connecion con el sicket servidor
        # LE decimos al cliente donde tienen que conectarse.
        client.connect(('0.0.0.0', 8000))
        
        # Esto funcion SEND nos pertmite enviar un paquete de datos al otro extremo de la coneccion.
        # Aqui se lo envio al servidor con el que acabo de conectarme
        
        # En cunato nos conectemos envio un mensage codificado
        client.send("Hello".encode())
        
        # Auqi recivo un paquete de datos con oun tamano fijo desde el otro extremo de la conneccion.
        # IMprimo lo que reciba del servidor
        print(client.recv(1024))
        
        
        try:
            # La respuesta que recibimos la metemos en un buclea a estar activo y enviando cosas hasta que yo te lo diga
            while True:
                
                # Esperamos un imput del ususario para enviar los mensajes al servidor
                message = input(">> ")
                
                # ENviamos el mensaje codificado
                # Esto funcion SEND nos pertmite enviar un paquete de datos al otro extremo de la coneccion.
                client.send(message.encode())
                
                # Recibo la respuesta del servidor.
                print("<< "+str(client.recv(1024)))
                
                # Si el mensage es close lo cerramos.
                if message == "close":
                    break
        finally:
            # Aqui cerramos nuestro cliente
            # Notifica al servidor que se va a cerrar.
            client.close()


if __name__ == "__main__":
    
    # La forma de probar este script es 
    
    #server = Server()
    client= Client()